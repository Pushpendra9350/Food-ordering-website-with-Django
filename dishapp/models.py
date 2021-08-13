from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dishes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    dishname = models.CharField(max_length=50)
    dishprice = models.FloatField()
    

