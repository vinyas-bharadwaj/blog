from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
  posts = Post.objects.all()
  context = {'posts': posts}
  return render(request, 'app/home.html', context=context)

def blog(request, pk):
  blog_post = Post.objects.get(id=pk)

  context = {'blog': blog_post}

  return render(request, 'app/blog.html', context=context)