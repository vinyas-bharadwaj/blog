from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('posts/<int:pk>', views.blog, name='posts'),
  path('posts/create', views.AddPost.as_view(), name='add-post'),
  path('posts/update/<int:pk>', views.UpdatePost.as_view(), name='update-post'),
  path('posts/<int:pk>/delete', views.DeletePost.as_view(), name='delete-post'),
]
