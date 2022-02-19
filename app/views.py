

import requests
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from msilib.schema import ListView
from multiprocessing import context
from typing import Generic
from unicodedata import category, name
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
API_KEY = '97154f0cb0fc4589b098a65ac9fa32d6'
# API_KEY = 'pub_4724aae0cedf2f08eeda566e3e5259d2f7a4'


# Create your views here.


def base(request):
    return render(request, 'base.html')


def home(request):
    #  country= request.GET.get('country')
    #  url = f'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=97154f0cb0fc4589b098a65ac9fa32d6'
    #  response = requests.get(url)
    #  data = response.json()
    
    #  articles = data['articles']

    #  context = {
    #     'articles': articles
    #  }
     url = f'https://newsdata.io/api/1/news?apikey=pub_4724aae0cedf2f08eeda566e3e5259d2f7a4&q=in&language=en'
     response = requests.get(url)
     data = response.json()
    
     results = data['results']

     context = {
         'results': results
     }
     return render(request, 'home.html',context)


def about(request):
    return render(request, 'about.html')


def blogs(request):
    return render(request, "blogs.html")


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = '__all__'
