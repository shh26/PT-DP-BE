# users/urls.py

from django.urls import path
from .views import ms_login_view, callback_view,signup,get_user,login,get_all_user,update_user,delete_user

urlpatterns = [
    path('ms_login/', ms_login_view, name='ms_login'),
    path('callback/', callback_view, name='callback'),
    path('signup/', signup, name='register-user'),
    path('profile/', get_user, name='get-user'),
    path('login/', login, name='login'),
    path('get_users/', get_all_user, name='get_all_user'),
    path('update/', update_user, name='update_user'),
    path('delete/<int:id>/', delete_user, name='delete_user'),




    ]
