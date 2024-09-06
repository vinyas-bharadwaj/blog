from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('posts/<int:pk>', views.blog, name='blog')
]
