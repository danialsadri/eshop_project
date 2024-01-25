from django.contrib import admin
from .models import Order, OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_date', 'is_paid']
    list_filter = ['is_paid']
    search_fields = ['user']
    raw_id_fields = ['user']


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'final_price', 'count']
    search_fields = ['order']
    raw_id_fields = ['order', 'product']
