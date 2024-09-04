from django.urls import path
from .views import OpportunityApiView

urlpatterns = [
    path('add/', OpportunityApiView.as_view(), name='opportunity_add'),   
    path('list/', OpportunityApiView.as_view(), name='opportunity_list'),
    path('<int:id>/', OpportunityApiView.as_view(), name='opportunity_detail'), 
    path('delete/<int:id>/', OpportunityApiView.as_view(), name='opportunity_delete'),
    path('edit/<int:id>/', OpportunityApiView.as_view(), name='opportunity_edit'),
]