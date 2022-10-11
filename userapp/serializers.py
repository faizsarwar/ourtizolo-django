from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
# User = get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','date_of_birth','phone_number','adress_line1', 'adress_line2','password','email','account_type','username']

class UserAdvisorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','phone_number','password','email','account_type','username','advisor_role','advisor_crd_number']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=(
            "id",
            "tittle",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )
