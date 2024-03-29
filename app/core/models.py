from django.contrib import admin
from django.conf import settings
from django.db import models
from uuid import uuid4
import os


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)

class Chef(models.Model):
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name 
    

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        
        
class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)  
    chef = models.ForeignKey(Chef, on_delete=models.SET_NULL, null=True)  
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    featured_collection = models.ForeignKey(
        'Collection', on_delete=models.SET_NULL, null=True,
        related_name='+', blank=True)
    
    def __str__(self):
        return self.name
    
    
class Collection(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, related_name='collections')
    featured_recipe = models.ForeignKey(
        'Recipe', on_delete=models.SET_NULL, null=True,
        related_name='+', blank=True)
    
    def __str__(self):
        return self.name
    
    
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    instructions = models.TextField(max_length=2048)
    time_minutes = models.PositiveIntegerField()
    Ingredients = models.ManyToManyField(Ingredient)
    created_at = models.DateTimeField(auto_now_add=True)
    collection = models.ManyToManyField(Collection, blank=True, related_name='recipes')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)
    
    def __str__(self):
        return self.title