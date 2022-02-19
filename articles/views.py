from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView ,  CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 


# Create your views here.
from django.views.generic import ListView
from .models import Article
class ArticleListView( LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView): 
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'



class ArticleUpdateView(LoginRequiredMixin,UpdateView):
      model = Article
      fields = ('title', 'body',)
      template_name = 'article_edit.html'
      login_url = 'login'
      success_url = reverse_lazy('article_list')

      def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)




class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    
class ArticleCreateView( LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    login_url = 'login'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
