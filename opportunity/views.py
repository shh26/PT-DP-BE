from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import OpportunitySerializer,CommentSerializer
from .models import Opportunity,OpportunityComment
from stcdp.common_pagination import PageNumberWithLimitPagination


class OpportunityApiView(APIView):
    pagination_class = PageNumberWithLimitPagination

    # Create Opportunity
    def post(self, request, id=None):
        try:
            # Create a new opportunity
            serializer = OpportunitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Opportunity.DoesNotExist:
            return Response({"message": "Opportunity does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    #update
    def patch(self, request, id=None):
        try:
            if not id:
                return Response({"message": "ID is required for updating an opportunity"}, status=status.HTTP_400_BAD_REQUEST)
            
            opportunity = Opportunity.objects.get(id=id)
            serializer = OpportunitySerializer(opportunity, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Opportunity updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Opportunity.DoesNotExist:
            return Response({"message": "Opportunity does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        

    # List or Retrieve Opportunity
    def get(self, request, id=None):
        try:
            if id:
                opportunity = Opportunity.objects.get(id=id)
                serializer = OpportunitySerializer(opportunity)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            queryset = Opportunity.objects.all().order_by('-created_at')
            
            # Search filter
            search_query = request.query_params.get('search', None)
            if search_query:
                queryset = queryset.filter(name__icontains=search_query)
            
            # Status filter
            status_filter = request.query_params.get('status', None)
            if status_filter:
                queryset = queryset.filter(status__icontains=status_filter)
            
            division_filter = request.query_params.get('division')
            if division_filter:
                queryset = queryset.filter(division_type__iexact=division_filter)
                
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = OpportunitySerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Opportunity.DoesNotExist:
            return Response({"message": "Opportunity not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    

    # Delete Opportunity
    def delete(self, request, id):
        try:
            opportunity = Opportunity.objects.get(id=id)
            opportunity.delete()
            return Response({"message": 'Opportunity deleted'}, status=status.HTTP_200_OK)
        except Opportunity.DoesNotExist:
            return Response({"message": 'Opportunity does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


class CommentApiView(APIView):
    pagination_class = PageNumberWithLimitPagination

    # Create Comment
    def post(self, request, id=None):
        try:
            # Create a new comment
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except OpportunityComment.DoesNotExist:
            return Response({"message": "Comment does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        
    # List or Retrieve comment
    def get(self, request, id=None):
        try:
            if id:
                opportunity = OpportunityComment.objects.get(id=id)
                serializer = CommentSerializer(opportunity)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            queryset = OpportunityComment.objects.all().order_by('-created_at')
            search_query = request.query_params.get('opportunity', None)
            if search_query:
                queryset = queryset.filter(opportunity__exact=search_query)
            
            # Status filter
            status_filter = request.query_params.get('status', None)
            if status_filter:
                queryset = queryset.filter(status__icontains=status_filter)
            
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except OpportunityComment.DoesNotExist:
            return Response({"message": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    

    # Delete Comment
    def delete(self, request, id):
        try:
            comment = OpportunityComment.objects.get(id=id)
            comment.delete()
            return Response({"message": 'Comment deleted'}, status=status.HTTP_200_OK)
        except OpportunityComment.DoesNotExist:
            return Response({"message": 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
