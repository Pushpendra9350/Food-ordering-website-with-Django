from django.db import models
from django.utils import timezone
# Create your models here.
class Placedorder(models.Model):
    user_id = models.CharField(max_length=10)
    restauro_id = models.CharField(max_length=10)
    dish = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    orderdate = models.DateTimeField(default=timezone.now)
