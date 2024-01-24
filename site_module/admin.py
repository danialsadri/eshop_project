from django.contrib import admin
from .models import SiteSetting, FooterLinkBox, FooterLink, Slider, SiteBanner


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'site_url', 'phone', 'email', 'is_main_setting']
    list_filter = ['is_main_setting']
    search_fields = ['site_name']


@admin.register(FooterLinkBox)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['footer_link_box', 'title', 'url']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'url_title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']


@admin.register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'url', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']
