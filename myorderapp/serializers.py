from rest_framework import serializers
from .models import Placedorder

class PlacedorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placedorder
        fields = '__all__'
    
class PlacemydorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placedorder
        fields = ['dish','price','orderdate']