from django.urls import path
from . import views

app_name = 'admin_panel'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_admin'),
    path('article/list/', views.ArticlesListView.as_view(), name='article_list_admin'),
    path('article/edit/<int:pk>/', views.ArticleEditView.as_view(), name='article_edit_admin'),
]
