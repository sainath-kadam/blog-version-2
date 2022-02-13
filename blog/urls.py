from django.urls import path
from .views import BlogListView , BlogDetailView


urlpatterns = [
path('post', BlogListView.as_view(), name='post'),
path('<int:pk>', BlogDetailView.as_view(), name='post_detail'),
 
]