from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BUS
from django.utils.translation import gettext as _
from users import models


class UserAdmin(BUS):
    ordering = ['id']
    list_display = ['id', 'email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields':('first_name','last_name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')
        }),
    )
    
    
admin.site.register(models.User, UserAdmin)
