from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('details/', order_details, name="order_details"),
    path('place/', place_order, name="place_order"),
    path('orders/', my_order_page, name="myorderpage"),
    path('myorders/', my_all_orders, name="myallorders"),
    #path('orders/', rest_order_page, name="restorderpage"),
    path('myorders/', rest_all_orders, name="restallorders")
]