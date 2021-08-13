from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from userapp.models import Userextension
from .models import Dishes
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .serializers import DishListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@login_required
def select_restaurant(request):
    currentuserobj = Userextension.objects.filter(user_id = request.user.id).first()
    if currentuserobj.usertype == "C":
        restaurants = []
        alluserobj = Userextension.objects.filter(usertype='R').all()
        for i in alluserobj:
            name = User.objects.filter(id = i.user_id).first().first_name
            user_id = User.objects.filter(id = i.user_id).first().id
            restaurants.append([name,user_id])
        context = {"restaurants":restaurants}
        return render(request, 'dishapp/selectrest.html',context=context)
    if currentuserobj.usertype == "R":
        # restaurants = []
        # alluserobj = Userextension.objects.filter(usertype='R').all()
        # for i in alluserobj:
        #     name = User.objects.filter(id = i.user_id).first().first_name
        #     user_id = User.objects.filter(id = i.user_id).first().id
        #     restaurants.append([name,user_id])
        # context = {"restaurants":restaurants}
        return render(request, 'myorderapp/restallorders.html',context={"restro":"yes"})
    
    

@login_required
@api_view(['POST'])
def get_dishes(request):
    print("Hello I not am here")
    if request.method == 'POST':
        all_dish_objects = Dishes.objects.filter(user_id = request.data['id']).all()
        restauro = User.objects.filter(id=request.data['id']).first()
        restauroname = restauro.first_name
        request.session['restauro_id'] = restauro.id
        alluserobj = Userextension.objects.filter(usertype='R').all()
        restaurants = []
        for i in alluserobj:
            name = User.objects.filter(id = i.user_id).first().first_name
            user_id = User.objects.filter(id = i.user_id).first().id
            restaurants.append([name,user_id])
        context = {"restaurants":restaurants,"dishes":all_dish_objects,"restauro":restauroname}
        return render(request, 'dishapp/selectrest.html',context=context)
    else:
        messages.success(request ,"Some thing went wrong")
        return redirect('restaurant')

# @login_required
# @api_view(['POST'])
# def placeorder(request):
#     if request.method == 'POST':
#         restaurant_code = request.data
#         all_dish_objects = Dishes.objects.filter(user_id = restaurant_code).all()
#         for i in all_dish_objects:
#             print(i.dishname)
#         return Response({"status":200,"message":"all good"})
#     else:
#         return Response({"status":400,"message":"It seems you are trying wrong type of request"})
