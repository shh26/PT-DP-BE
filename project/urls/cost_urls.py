from django.urls import path
from ..views import CostApiView

urlpatterns = [
    path('add/', CostApiView.as_view(), name='cost_add'),   
    path('list/', CostApiView.as_view(), name='cost_list'),
    path('<id>/', CostApiView.as_view(), name='cost_detail'), 
    path('delete/<id>/', CostApiView.as_view(), name='cost_delete'),
    path('edit/<id>/', CostApiView.as_view(), name='cost_edit'),
]