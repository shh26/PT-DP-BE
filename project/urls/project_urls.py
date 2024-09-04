from django.urls import path
from ..views import ProjectApiView

urlpatterns = [
    path('add/', ProjectApiView.as_view(), name='project_add'),   
    path('list/', ProjectApiView.as_view(), name='project_list'),
    path('<int:id>/', ProjectApiView.as_view(), name='project_detail'), 
    path('delete/<int:id>/', ProjectApiView.as_view(), name='project_delete'),
    path('edit/<int:id>/', ProjectApiView.as_view(), name='project_edit'),
]