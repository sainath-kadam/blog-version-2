from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.edit import CreateView
from .views import *

urlpatterns = [
   
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',ContactCreateView.as_view(), name='contact_new'),
    path('blogs/', views.blogs, name='blogs'),
]