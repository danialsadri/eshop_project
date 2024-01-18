from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']
    readonly_fields = ['email_active_code']
    ordering = ['email']

    fieldsets = [
        ('اطلاعات', {'fields': ['username', 'email', 'password']}),
        ('اطلاعات شخصی', {'fields': ['first_name', 'last_name']}),
        ('دسترسی ها', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
        ('اطلاعات تکمیلی', {'fields': ['email_active_code', 'about_user', 'address', 'avatar']}),
    ]
