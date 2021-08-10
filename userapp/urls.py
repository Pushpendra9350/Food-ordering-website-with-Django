from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('register_user/', register_user, name="register_user"),

]