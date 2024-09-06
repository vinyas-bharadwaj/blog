from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Post
from .forms import CreatePost, EditPost
# from .mlmodel import classifier

# Create your views here.
def home(request):
  posts = Post.objects.all()
  context = {'posts': posts}
  return render(request, 'app/home.html', context=context)

def blog(request, pk):
  blog_post = Post.objects.get(id=pk)

  context = {'blog': blog_post}

  return render(request, 'app/blog.html', context=context)

class AddPost(CreateView):
  model = Post
  form_class = CreatePost
  template_name = 'app/add-post.html'
  # fields = ['title', 'body', 'author']

class UpdatePost(UpdateView):
  model = Post
  form_class = EditPost
  template_name = 'app/update-post.html'
  # fields = ['title', 'body']