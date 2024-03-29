from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import *
from users.models import User


class ChefSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, source='user.username')
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    
    class Meta:
        model = Chef
        fields = ['user_id','birth_date', 'user']
        

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name']
        
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'collections_count']
        read_only_fields = ['id',]
        
    collections_count = serializers.IntegerField(read_only=True)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'recipes_count']
        
    recipes_count = serializers.IntegerField(read_only=True)
    
    
class RecipeSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'instructions', 'time_minutes', 'Ingredients', 'created_at', 'collection', 'image']
        read_only_fields = ['id',]
        
class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipes"""

    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_fields = ['id',]