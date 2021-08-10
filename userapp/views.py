from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import NewUserSerializer, UserExtensionSerializer
from .forms import userExtensionForm, userRegisterForm
import django

# Create your views here.
def register(request):
    ue = userExtensionForm()
    u = userRegisterForm()
    context = {"user":u,"userext":ue}
    return render(request,'userapp/register.html',context=context)
def login(request):
    return render(request,'userapp/login.html')


@api_view(['GET'])
def login_user(request):
    if request.method == 'GET':
        users_objs = User.objects.all()
        serializer = NewUserSerializer(users_objs,many=True)
        return Response({"status":200,"payload":serializer.data})
    return Response({"message":"hello world"})

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        
        serializer1 = NewUserSerializer(data=request.data)

        serializer2 = UserExtensionSerializer(data = request.data)
        print("this is a request-----------",request.User)
        print(serializer1)
        if not serializer1.is_valid():
            return Response({"status":400,"message":serializer1.errors})
        if not serializer2.is_valid():
            return Response({"status":400,"message":"Something went wrong"})
        serializer1.save()
        serializer2.save()

        return Response({"status":200,"Message":"You have registered successfully"})
    
    