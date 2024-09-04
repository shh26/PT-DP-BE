from django.urls import path
from ..views import DecisionLogApiView

urlpatterns = [
    path('add/', DecisionLogApiView.as_view(), name='decision_add'),   
    path('list/', DecisionLogApiView.as_view(), name='decision_list'),
    path('<id>/', DecisionLogApiView.as_view(), name='decision_detail'), 
    path('delete/<id>/', DecisionLogApiView.as_view(), name='decision_delete'),
    path('edit/<id>/', DecisionLogApiView.as_view(), name='decision_edit'),
]