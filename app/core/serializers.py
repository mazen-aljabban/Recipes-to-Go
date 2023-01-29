from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'first_name', 'last_name']
        

class ChefSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    
    
    class Meta:
        model = Chef
        fields = ['id', 'user_id','birth_date']
        

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name']