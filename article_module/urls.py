from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('list/', views.ArticlesListView.as_view(), name='articles_list'),
    path('list/cat/<str:category>/', views.ArticlesListView.as_view(), name='articles_by_category_list'),
    path('detail/<int:pk>/', views.ArticleDetailView.as_view(), name='articles_detail'),
    path('add-article-comment/', views.add_article_comment, name='add_article_comment'),
]
