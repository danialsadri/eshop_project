from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home_module.urls', namespace='home')),
    path('accounts/', include('account_module.urls', namespace='accounts')),
    path('articles/', include('article_module.urls', namespace='articles')),
    path('contact_us/', include('contact_module.urls', namespace='contact_us')),
    path('products/', include('product_module.urls', namespace='products')),
    path('users/', include('user_panel_module.urls', namespace='users')),
    path('orders/', include('order_module.urls', namespace='orders')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.sites.AdminSite.site_title = "پنل مدیریت"
admin.sites.AdminSite.site_header = "پنل مدیریت"
admin.sites.AdminSite.index_title = "پنل مدیریت"
