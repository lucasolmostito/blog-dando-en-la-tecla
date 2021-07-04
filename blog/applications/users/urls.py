#
from django.urls import path

from . import views

app_name = "app_users"

urlpatterns = [
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'update/', 
        views.UpdatePasswordView.as_view(),
        name='user-update',
    ),
    path(
        'update-info/<pk>/', 
        views.UpdateInfoUserView.as_view(),
        name='user-info-update',
    ),
]