from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProjectSerializer,DecisionLogSerializer,RiskSerializer,CostSerializer,FeedbackSerializer
from .models import Project,DecisionLog,Risk,Costs,ProjectFeedback
from stcdp.common_pagination import PageNumberWithLimitPagination
from rest_framework.permissions import IsAuthenticated

#Project Api View
class ProjectApiView(APIView):
    #permission_classes = [IsAuthenticated]
    pagination_class = PageNumberWithLimitPagination

    # Create Project
    def post(self, request, id=None):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"message": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    #update
    def patch(self, request, id=None):
        try:
            if not id:
                return Response({"message": "ID is required for updating a project"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Fetch the existing project
            project = Project.objects.get(id=id)
            
            # Prepare the data for partial update
            data = request.data.copy()
            
            # Handle the team_member field separately
            team_member_ids = data.pop('team_member', None)
            serializer = ProjectSerializer(project, data=data, partial=True)
            
            if serializer.is_valid():
                updated_project = serializer.save()
                
                # Update the team_member field
                if team_member_ids is not None:
                    updated_project.team_member.set(team_member_ids)
                
                return Response({"message": "Project updated successfully", "data": ProjectSerializer(updated_project).data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"message": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        

    # List or Retrieve project
    def get(self, request, id=None):
        try:
            if id:
                try:
                    project = Project.objects.get(id=id)
                    serializer = ProjectSerializer(project)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Project.DoesNotExist:
                    return Response({"message": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
            
            queryset = Project.objects.all().order_by('-created_at')
            
            # Search filter
            search_query = request.query_params.get('search')
            if search_query:
                queryset = queryset.filter(name__icontains=search_query)
            
            # Status filter
            status_filter = request.query_params.get('status')
            if status_filter:
                queryset = queryset.filter(status__iexact=status_filter)
            
            division_filter = request.query_params.get('division')
            if division_filter:
                queryset = queryset.filter(division_type__iexact=division_filter)
            
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = ProjectSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Delete Project
    def delete(self, request, id):
        try:
            opportunity = Project.objects.get(id=id)
            opportunity.delete()
            return Response({"message": 'Project deleted'}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({"message": 'Project does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        


#Decision Log Api View
class DecisionLogApiView(APIView):
    #permission_classes = [IsAuthenticated]
    pagination_class = PageNumberWithLimitPagination

    # Create Project
    def post(self, request, id=None):
        try:
            serializer = DecisionLogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DecisionLog.DoesNotExist:
            return Response({"message": "Decision log does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    #update
    def patch(self, request, id=None):
        try:
            if not id:
                return Response({"message": "ID is required for updating an decision log"}, status=status.HTTP_400_BAD_REQUEST)
            
            decision_log = DecisionLog.objects.get(id=id)
            serializer = DecisionLogSerializer(decision_log, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Decision Log updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DecisionLog.DoesNotExist:
            return Response({"message": "Decision log does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        

    # List or Retrieve Decision log
    def get(self, request, id=None):
        try:
            if id:
                try:
                    decsion_log = DecisionLog.objects.get(id=id)
                    serializer = DecisionLogSerializer(decsion_log)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except DecisionLog.DoesNotExist:
                    return Response({"message": "Decision log not found"}, status=status.HTTP_404_NOT_FOUND)
            
            queryset = DecisionLog.objects.all().order_by('-created_at')
            
            # Search filter
            search_query = request.query_params.get('search')
            if search_query:
                queryset = queryset.filter(detail__icontains=search_query)
            
            # Status filter
            status_filter = request.query_params.get('status')
            if status_filter:
                queryset = queryset.filter(status__iexact=status_filter)
            
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = DecisionLogSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Delete Decsion Log
    def delete(self, request, id):
        try:
            decison_log = DecisionLog.objects.get(id=id)
            decison_log.delete()
            return Response({"message": 'Decision Log deleted'}, status=status.HTTP_200_OK)
        except DecisionLog.DoesNotExist:
            return Response({"message": 'Decision log does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        




#Risk Api View
class RiskApiView(APIView):
    #permission_classes = [IsAuthenticated]
    pagination_class = PageNumberWithLimitPagination

    # Create Risk
    def post(self, request, id=None):
        try:
            serializer = RiskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Risk.DoesNotExist:
            return Response({"message": "Risk log does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    #update
    def patch(self, request, id=None):
        try:
            if not id:
                return Response({"message": "ID is required for updating an risk"}, status=status.HTTP_400_BAD_REQUEST)
            
            risk = Risk.objects.get(id=id)
            serializer = RiskSerializer(risk, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Risk updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Risk.DoesNotExist:
            return Response({"message": "Risk does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        

    # List or Retrieve Risk
    def get(self, request, id=None):
        try:
            if id:
                try:
                    decsion_log = Risk.objects.get(id=id)
                    serializer = RiskSerializer(decsion_log)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Risk.DoesNotExist:
                    return Response({"message": "Risk not found"}, status=status.HTTP_404_NOT_FOUND)
            
            queryset = Risk.objects.all().order_by('-created_at')
            
            # Search filter
            search_query = request.query_params.get('search')
            if search_query:
                queryset = queryset.filter(name__icontains=search_query)
            
            # # category filter
            category_filter = request.query_params.get('category')
            if category_filter:
                queryset = queryset.filter(category__iexact=category_filter)
            
            #project filter
            project_filter = request.query_params.get('project')
            if project_filter:
                queryset = queryset.filter(project__exact=project_filter)
            
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = RiskSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Delete Decsion Log
    def delete(self, request, id):
        try:
            risk = Risk.objects.get(id=id)
            risk.delete()
            return Response({"message": 'Risk deleted'}, status=status.HTTP_200_OK)
        except Risk.DoesNotExist:
            return Response({"message": 'Risk does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        




#Cost Api View
class CostApiView(APIView):
    #permission_classes = [IsAuthenticated]
    pagination_class = PageNumberWithLimitPagination

    # Create Cost
    def post(self, request, id=None):
        try:
            serializer = CostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Costs.DoesNotExist:
            return Response({"message": "Cost does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    #update
    def patch(self, request, id=None):
        try:
            if not id:
                return Response({"message": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            cost = Costs.objects.get(id=id)
            serializer = CostSerializer(cost, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Cost updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Risk.DoesNotExist:
            return Response({"message": "Cost does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        

    # List or Retrieve Cost
    def get(self, request, id=None):
        try:
            if id:
                try:
                    cost = Costs.objects.get(id=id)
                    serializer = CostSerializer(cost)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Costs.DoesNotExist:
                    return Response({"message": "Cost not found"}, status=status.HTTP_404_NOT_FOUND)
            
            queryset = Costs.objects.all().order_by('-created_at')
            
            # Search filter
            search_query = request.query_params.get('search')
            if search_query:
                queryset = queryset.filter(name__icontains=search_query)
            
            #division filter
            division_filter = request.query_params.get('division')
            if division_filter:
                queryset = queryset.filter(project__division_type__iexact=division_filter)
            
            project_filter = request.query_params.get('project')
            if project_filter:
                queryset = queryset.filter(project__exact=project_filter)
            
            
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = CostSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Delete Cost
    def delete(self, request, id):
        try:
            cost = Costs.objects.get(id=id)
            cost.delete()
            return Response({"message": 'Cost deleted'}, status=status.HTTP_200_OK)
        except Costs.DoesNotExist:
            return Response({"message": 'Cost does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)





#Cost Api View
class FeedbackApiView(APIView):
    #permission_classes = [IsAuthenticated]
    pagination_class = PageNumberWithLimitPagination

    # Create Feedback
    def post(self, request, id=None):
        try:
            serializer = FeedbackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProjectFeedback.DoesNotExist:
            return Response({"message": "Feedback does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    #update
    def patch(self, request, id=None):
        try:
            if not id:
                return Response({"message": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            cost = ProjectFeedback.objects.get(id=id)
            serializer = FeedbackSerializer(cost, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Feedback updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProjectFeedback.DoesNotExist:
            return Response({"message": "Feedback does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        

    # List or Retrieve Feedback
    def get(self, request, id=None):
        try:
            if id:
                try:
                    feedback = ProjectFeedback.objects.get(id=id)
                    serializer = FeedbackSerializer(feedback)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except ProjectFeedback.DoesNotExist:
                    return Response({"message": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)
            
            queryset = ProjectFeedback.objects.all().order_by('-created_at')
            
            # Search filter
            search_query = request.query_params.get('search')
            if search_query:
                queryset = queryset.filter(name__icontains=search_query)
            
            # Feedback filter
            project_filter = request.query_params.get('project')
            if project_filter:
                queryset = queryset.filter(project__exact=project_filter)
            
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = FeedbackSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        
        except Exception as e:
            return Response({"message": f"Something went wrong: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Delete Feedback
    def delete(self, request, id):
        try:
            feedback = ProjectFeedback.objects.get(id=id)
            feedback.delete()
            return Response({"message": 'Feedback deleted'}, status=status.HTTP_200_OK)
        except ProjectFeedback.DoesNotExist:
            return Response({"message": 'Feedback does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f'Something went wrong: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)