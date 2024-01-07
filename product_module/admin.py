from django.contrib import admin
from .models import *


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']
    search_fields = ['title']


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']
    search_fields = ['title', 'short_description', 'description']
    list_editable = ['price', 'is_active', 'is_delete']
    raw_id_fields = ['brand']
    prepopulated_fields = {'slug': ['title']}


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['product', 'caption']
    list_filter = ['product']
    search_fields = ['product', 'caption']
    raw_id_fields = ['product']


@admin.register(ProductVisit)
class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'ip']
    list_filter = ['user', 'product', 'ip']
    raw_id_fields = ['user', 'product']
    search_fields = ['user', 'product', 'ip']


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']
    list_filter = ['product']
    raw_id_fields = ['product']
    search_fields = ['product']
