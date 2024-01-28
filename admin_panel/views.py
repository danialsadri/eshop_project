from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, TemplateView
from article_module.models import Article
from utils.my_decorators import permission_checker_decorator_factory


@method_decorator(permission_checker_decorator_factory({'permission_name': 'home'}), name='dispatch')
class HomeView(TemplateView):
    template_name = 'admin_panel/home/home.html'


@method_decorator(permission_checker_decorator_factory({'permission_name': 'article_list'}), name='dispatch')
class ArticlesListView(ListView):
    model = Article
    template_name = 'admin_panel/articles/article_list.html'
    context_object_name = 'articles'


@method_decorator(permission_checker_decorator_factory({'permission_name': 'article_edit'}), name='dispatch')
class ArticleEditView(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'admin_panel/articles/article_edit.html'
    success_url = reverse_lazy('admin_panel:article_list_admin')
