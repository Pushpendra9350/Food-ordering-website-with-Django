from django.db import models
from django.contrib.auth.models import User



class Userextension(models.Model):
    user_type= [
        ('C', 'Normal User'),
        ('R', 'Restaurant')]
    usertype = models.CharField(max_length = 1,choices = user_type)
    address = models.CharField(max_length = 100)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    





