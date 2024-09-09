from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('posts/<int:pk>', views.blog, name='posts'),
  path('posts/create', views.AddPost.as_view(), name='add-post'),
  path('add-category', views.AddCategory.as_view(), name='add-category'),
  path('posts/<str:cats>', views.categoryPosts, name='category-posts'),
  path('posts/update/<int:pk>', views.UpdatePost.as_view(), name='update-post'),
  path('posts/delete/<int:pk>', views.DeletePost.as_view(), name='delete-post'),
]
