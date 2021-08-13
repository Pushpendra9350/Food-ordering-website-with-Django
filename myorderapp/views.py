from django.shortcuts import render
from rest_framework.decorators import api_view
from dishapp.models import Dishes
from .models import Placedorder
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import PlacedorderSerializer, PlacemydorderSerializer
from userapp.models import Userextension
from django.http import JsonResponse
import json
# Create your views here.

@login_required
@api_view(['POST'])
def order_details(request):
    if request.method == "POST":
        data = request.POST
        data=data.dict()
        request.session['dish_ids'] = data['id']
        dish_list = []
        price = 0
        for i in data['id']:
            dish_objs = Dishes.objects.filter(id = i).first()
            dish_list.append(dish_objs.dishname)
            price+=dish_objs.dishprice
        rest_name = User.objects.filter(id = request.session['restauro_id']).first().first_name
        rest_address = Userextension.objects.filter(user_id = request.session['restauro_id']).first().address
        user_address = Userextension.objects.filter(user_id = request.user.id).first().address
        context={"price":price,"dishes":dish_list[0],"restname":rest_name,"restaddress":rest_address,"user_address":user_address}
        return render(request, 'myorderapp/orderdetails.html',context=context)
    return Response({"status":400,"message":"something went wrong"})


@login_required
@api_view(['POST'])
def place_order(request):
    if request.method == "POST":
        data = {}
        data["user_id"] = request.user.id
        data["restauro_id"] = request.session['restauro_id']
        dishobj = Dishes.objects.filter(id=request.session['dish_ids']).first()
        data["dish"] = dishobj.dishname
        data["price"] = dishobj.dishprice
        serializer = PlacedorderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'myorderapp/confirm.html',context={"orderplced":"Your Order is successfully places"})
    return Response({"status":400,"message":"something went wrong"})

@login_required       
@api_view(['GET'])
def my_all_orders(request):
    if request.method == "GET":
        dataobjs = Placedorder.objects.filter(user_id = request.user.id).all().values()
        final_data = []
        for i in range(len(dataobjs)):
            one_recd = {}
            one_recd["dish"] = dataobjs[i]["dish"]
            one_recd["price"] = dataobjs[i]["price"]
            one_recd["date"] = dataobjs[i]["orderdate"]
            final_data.append(one_recd)
    return JsonResponse(final_data,safe=False)

@login_required       
@api_view(['GET'])
def rest_all_orders(request):
    if request.method == "GET":
        dataobjs = Placedorder.objects.filter(restauro_id = request.user.id).all().values()
        print(dataobjs)
        final_data = []
        total = 0
        for i in range(len(dataobjs)):
            one_recd = {}
            one_recd["dish"] = dataobjs[i]["dish"]
            one_recd["price"] = dataobjs[i]["price"]
            total += dataobjs[i]["price"]
            one_recd["date"] = dataobjs[i]["orderdate"]
            final_data.append(one_recd)
        final_data.append({"total":total})
    return JsonResponse(final_data,safe=False)

@login_required()
def my_order_page(request):
   return render(request,'myorderapp/myallorders.html')
   
@login_required()
def rest_order_page(request):
   return render(request,'myorderapp/restallorders.html')
   