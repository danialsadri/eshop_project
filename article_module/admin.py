from django.contrib import admin
from django.http import HttpRequest
from .models import ArticleCategory, Article, ArticleComment


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'url_title']
    list_editable = ['is_active']
    raw_id_fields = ['parent']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    list_editable = ['is_active']
    raw_id_fields = ['author', 'categories']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['parent', 'article', 'user', 'create_date']
    list_filter = ['create_date']
    search_fields = ['text']
    raw_id_fields = ['parent', 'article', 'user']
