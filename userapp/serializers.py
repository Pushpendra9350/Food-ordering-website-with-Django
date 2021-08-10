from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Userextension
from django.core.validators import validate_email


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, data):
        if data["first_name"]:
            for i in data["first_name"]:
                if i.isdigit():
                    raise serializers.ValidationError({"error":"Name does not conatin numeric values"})
        # if not validate_email(data['email']):
        #     raise serializers.ValidationError({"error":"Email is in wrong format"})
        return data
    
class UserExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userextension
        fields = '__all__'
    