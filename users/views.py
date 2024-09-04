# users/views.py

from django.shortcuts import redirect
from django.conf import settings
from msal import ConfidentialClientApplication
from django.contrib.auth import login, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate
User = get_user_model()
from stcdp.common_pagination import PageNumberWithLimitPagination
from importlib import reload

#Register user
@api_view(['POST'])
def signup(request):
    try:
        if request.method == 'POST':
            print(request.data,'?????????????data')
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



#get single user
@api_view(['POST'])
def get_user(request):
    try:
        if request.method == 'POST':
            email = request.data.get('email')
            if email:
                user = User.objects.get(email=email) 
                if user:
                    serializer = CustomUserSerializer(user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'ms_id not provided in request data'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


#Login
@api_view(['GET','POST'])
def ms_login_view(request):
    redirect_uri = settings.AZURE_REDIRECT_URI
    client = ConfidentialClientApplication(
        client_id=settings.AUTH_ADFS['CLIENT_ID'],
        
        authority=f"https://login.microsoftonline.com/{settings.AUTH_ADFS['TENANT_ID']}",
    )
    
    auth_url = client.get_authorization_request_url(
        scopes=["User.Read"],
        redirect_uri=redirect_uri,
    )
    return Response({'auth_url': auth_url})


#Callback 
@api_view(['GET','POST'])
def callback_view(request):
    redirect_uri = settings.AZURE_REDIRECT_URI
    data = json.loads(request.body)
    code = data.get('code', None)
    if not code:
        return Response({'error': 'Authorization code not provided'}, status=status.HTTP_400_BAD_REQUEST)

    client = ConfidentialClientApplication(
        client_id=settings.AUTH_ADFS['CLIENT_ID'],
        authority=f"https://login.microsoftonline.com/{settings.AUTH_ADFS['TENANT_ID']}",
    )

    try:
        token_response = client.acquire_token_by_authorization_code(
            code=code,
            scopes=["User.Read"],
            redirect_uri=redirect_uri,
        )
    except Exception as e:
        return Response({'error': f'Error fetching token: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if 'access_token' in token_response:
        access_token = token_response['access_token']
        frontend_redirect_url = f"{redirect_uri}?access_token={access_token}"
        print(frontend_redirect_url)
        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
    else:
        error_description = token_response.get('error_description', 'Unknown error')
        return Response({'error': f'Error in token response: {error_description}'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        email = request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            return Response({"error":"email and password is required"},status=status.HTTP_400_BAD_REQUEST)
        user=authenticate(request,username=email,password=password)
        #user = User.objects.filter(email=email).first()
       # print(user,'???????')
        if user is not None:
            serializer=CustomUserSerializer(user)
            return Response({"data":serializer.data},status=status.HTTP_200_OK)
        else:

            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['GET'])
def get_all_user(request):
    pagination_class = PageNumberWithLimitPagination
    try:
        users = User.objects.all()
        if users:
            paginator = pagination_class()
            paginated_queryset = paginator.paginate_queryset(users, request)
            serializer = CustomUserSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    


#update single user
@api_view(['POST'])
def update_user(request):
    user_id = request.data.get('id')
    if not user_id:
        return Response({'error': 'ID required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CustomUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)