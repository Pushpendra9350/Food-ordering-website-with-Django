from django import forms
from django.contrib.auth.models import User
from .models import Userextension
from django.contrib.auth.forms import UserCreationForm


class userRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","username","email"]
        labels = {'first_name':'Name', 'username':'Username','email':'Email'}
class userExtensionForm(forms.ModelForm):
    class Meta:
        model = Userextension
        fields = ['usertype','address']
        labels = {'usertype':'User Type', 'address':'Address'}
