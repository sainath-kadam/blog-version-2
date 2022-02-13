from ast import Str
from email.policy import default
from enum import auto, unique

from random import choice, choices
from telnetlib import STATUS
from turtle import title

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50) 
    email = models.EmailField()
    phone=models.CharField(max_length=12,null=True)
    desc = models.TextField()
    def __str__(self):
        return self.name
    def get_absolute_url(self): 
        return reverse('contact_new', args=[str(self.id)])

