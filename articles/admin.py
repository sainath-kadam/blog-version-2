

# Register your models here.
from django.contrib import admin
from .models import Article,Comment



admin.site.register(Comment)
 
 

class CommentInline(admin.StackedInline): # new
    model = Comment
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [CommentInline,]


class CommentInline(admin.TabularInline): # new
    model = Comment
admin.site.register(Article,ArticleAdmin)