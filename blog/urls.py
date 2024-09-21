from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
  
    path('posts/', views.all_posts, name='all_posts'),
  
    path('posts/<slug:slug>', views.post_details, name='post_details_page')
]