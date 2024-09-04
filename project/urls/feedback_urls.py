from django.urls import path
from ..views import FeedbackApiView

urlpatterns = [
    path('add/', FeedbackApiView.as_view(), name='feedback_add'),   
    path('list/', FeedbackApiView.as_view(), name='feedback_list'),
    path('<id>/', FeedbackApiView.as_view(), name='feedback_detail'), 
    path('delete/<id>/', FeedbackApiView.as_view(), name='feedback_delete'),
    path('edit/<id>/', FeedbackApiView.as_view(), name='feedback_edit'),
]