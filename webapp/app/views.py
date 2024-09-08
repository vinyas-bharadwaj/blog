from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CreatePost, EditPost
# from .mlmodel import classifier

# Create your views here.
def home(request):
  posts = Post.objects.all().order_by('-created_at')
  cat_menu = Category.objects.all()

  context = {'posts': posts, 'cat_menu': cat_menu}

  return render(request, 'app/home.html', context=context)

def blog(request, pk):
  blog_post = Post.objects.get(id=pk)

  context = {'blog': blog_post}

  return render(request, 'app/blog.html', context=context)

def categoryPosts(request, cats):
  cats = cats.replace('-', ' ') # we need to replace the '-' with ' ' since we slugified the url
  posts = Post.objects.filter(category=cats).all()
  cat_menu = Category.objects.all()

  context = {'posts': posts, 'category': cats.title(), 'cat_menu': cat_menu}

  return render(request, 'app/category-posts.html', context = context)

class AddPost(CreateView):
  model = Post
  form_class = CreatePost
  template_name = 'app/add-post.html'
  # fields = ['title', 'body', 'author']

class AddCategory(CreateView):
  model = Category
  fields = '__all__'
  template_name = 'app/add-category.html' 

class UpdatePost(UpdateView):
  model = Post
  form_class = EditPost
  template_name = 'app/update-post.html'
  # fields = ['title', 'body']

class DeletePost(DeleteView):
  model = Post
  template_name = 'app/delete-post.html'
  success_url = reverse_lazy('home')