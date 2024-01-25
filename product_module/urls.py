from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product-list'),
    path('list/cat/<cat>/', views.ProductListView.as_view(), name='product-categories-list'),
    path('list/brand/<brand>/', views.ProductListView.as_view(), name='product-list-by-brands'),
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]
