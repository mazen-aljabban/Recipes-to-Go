from django.contrib import admin
from django.conf import settings
from django.db import models
from uuid import uuid4
from users.models import User

# Create your models here.

class Chef(models.Model):
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
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
        