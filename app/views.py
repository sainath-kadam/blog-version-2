

from msilib.schema import ListView
from typing import Generic
from unicodedata import name
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


from django.http import HttpResponse

from django.views import generic

# Create your views here.
from django.shortcuts import render
def base(request):
   return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request,'about.html')  
def blogs(request):
    return render(request, "blogs.html") 
    
    

    



class ContactCreateView(CreateView): 
    model = Contact
    template_name = 'contact.html'
    fields = '__all__'

