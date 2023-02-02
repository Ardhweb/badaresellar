from django.urls import path
from . import views

from .models import Post

urlpatterns = [
    path('', views.blog_page, name='blog-page'),
    path('<int:id>/', views.post_detail, name='post-detail'),
    
]
