from django.urls import path
from .views import CommentApiView

urlpatterns = [
    path('add/', CommentApiView.as_view(), name='comment_add'),   
    path('list/', CommentApiView.as_view(), name='comment_list'),
    path('delete/<int:id>/', CommentApiView.as_view(), name='comment_delete'),
    path('edit/<int:id>/', CommentApiView.as_view(), name='comment_edit'),
]