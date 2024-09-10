from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Category
from .forms import CreatePost, EditPost
from django.http import HttpResponseRedirect

# Home Page
def home(request):
  posts = Post.objects.all().order_by('-created_at')
  cat_menu = Category.objects.all()

  context = {'posts': posts, 'cat_menu': cat_menu}

  return render(request, 'app/home.html', context=context)

# Singular blog details
def blog(request, pk):
  blog_post = Post.objects.get(id=pk)

  liked_users = get_object_or_404(Post, id=pk)

  liked = False
  if liked_users.likes.filter(id=request.user.id).exists():
    liked = True

  context = {'blog': blog_post, 'liked': liked}

  return render(request, 'app/blog.html', context=context)

# Blog posts filtered by category
def categoryPosts(request, cats):
  cats = cats.replace('-', ' ') # we need to replace the '-' with ' ' since we slugified the url
  posts = Post.objects.filter(category=cats).all()
  cat_menu = Category.objects.all()

  context = {'posts': posts, 'category': cats.title(), 'cat_menu': cat_menu}

  return render(request, 'app/category-posts.html', context = context)

# Liking a post
def LikePost(request, pk):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))

  # If the post has already been liked by the user, We need to remove the like 
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)

  # If the user has not liked the post yet, it function normally
  else:
    post.likes.add(request.user)

  return HttpResponseRedirect(reverse('posts', args=[str(pk)])) 

# Page to add a new post
class AddPost(CreateView):
  model = Post
  form_class = CreatePost
  template_name = 'app/add-post.html'
  # fields = ['title', 'body', 'author']

# Page to add new category
class AddCategory(CreateView):
  model = Category
  fields = '__all__'
  template_name = 'app/add-category.html' 

# Page to update a blog post
class UpdatePost(UpdateView):
  model = Post
  form_class = EditPost
  template_name = 'app/update-post.html'
  # fields = ['title', 'body']

# Page to delete a post
class DeletePost(DeleteView):
  model = Post
  template_name = 'app/delete-post.html'
  success_url = reverse_lazy('home')