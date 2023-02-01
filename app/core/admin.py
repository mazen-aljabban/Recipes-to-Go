from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.urls import reverse
from tags.models import TaggedItem
from . import models

# Register your models here.
@admin.register(models.Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    readonly_fields = ['join_date']
    
    
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    
    
@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_per_page = 10
    inlines = [TagInline]
    search_fields = ['title__istartwith']
    

@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10
    search_fields = ['name__istartswith']
    
    
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10
    search_fields = ['name__starswith']
    
    
@admin.register(models.Category)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10
    search_fields = ['name__starswith']