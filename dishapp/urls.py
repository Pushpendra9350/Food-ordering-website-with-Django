from django.urls import path
from .views import *

urlpatterns = [
    path('', select_restaurant, name="restaurant"),
    path('all_dishes/', get_dishes, name="getdishes"),

]