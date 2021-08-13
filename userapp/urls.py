from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login, name="login"),
    path('login_user/', login_user, name="login_user"),
    path('register/', register, name="register"),
    path('register_user/', register_user, name="register_user"),
    path('logout/', auth_views.LogoutView.as_view(template_name="homeapp/index.html"), name="logout")
]