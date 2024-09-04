from django.urls import path
from ..views import RiskApiView

urlpatterns = [
    path('add/', RiskApiView.as_view(), name='risk_add'),   
    path('list/', RiskApiView.as_view(), name='risk_list'),
    path('<id>/', RiskApiView.as_view(), name='risk_detail'), 
    path('delete/<id>/', RiskApiView.as_view(), name='risk_delete'),
    path('edit/<id>/', RiskApiView.as_view(), name='risk_edit'),
]