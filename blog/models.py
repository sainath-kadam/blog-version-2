from django.db import models

# Create your models here.







class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
     ordering = ['-date',]

def __str__(self):
    return self.title








