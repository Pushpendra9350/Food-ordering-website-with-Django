from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from .models import Userextension
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .serializers import NewUserSerializer, UserExtensionSerializer
from .forms import userExtensionForm, userRegisterForm
import django
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def register(request):
    ue = userExtensionForm()
    u = userRegisterForm(   )
    context = {"user":u,"userext":ue}
    return render(request,'userapp/register.html',context=context)
def login(request):
    return render(request,'userapp/login.html')


@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        logged_in_user = auth.authenticate(username = request.data['username'],password=request.data['password'])
        if logged_in_user is not None:
            auth.login(request,logged_in_user)
            #usertype = Userextension.objects.filter(user_id = logged_in_user.id).first()
            #return render(request, 'dishapp/selectrest.html',context={"usertype":usertype.usertype})
            return redirect('restaurant')
        else:
            return render(request, "userapp/login.html", context = {"log_message":"Username or password is wrong!"})
    else:
        return render(request,'userapp/login.html')

@api_view(['POST'])
def register_user(request):
    if request.is_ajax and request.method == 'POST':
        data1 = request.data
        # Here we copy this QueryDict to make it immutable
        data2 = data1.copy()
        data2["password"] = make_password(data2['password'])
        data2["is_active"] = True
        serializer1 = NewUserSerializer(data=data2)
        if not serializer1.is_valid():
            try:
                if serializer1.errors:
                    messages.success(request, serializer1.errors['error'][0])
                    return redirect('register')
            except:
                if serializer1.errors:
                    messages.success(request, serializer1.errors['username'][0])
                    return redirect('register')
        email = User.objects.filter(email=data2['email'])
        if email:
            messages.success(request, "Email is already user! please try with another one")
            return redirect('register')
        serializer1.save()
        data2["user"] = serializer1['id'].value
        serializer2 = UserExtensionSerializer(data = data2)
        if not serializer2.is_valid():
            return render(request,"userapp/register.html", context = {"reg_message":"There is some Problem! from your end"})
        serializer2.save()
        return render(request,"userapp/login.html", context = {"reg_message":"You have registered successfully! Login to continue"})
    
    