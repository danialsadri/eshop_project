from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'full_name', 'created_date']
    list_filter = ['created_date']
    search_fields = ['title', 'full_name']
