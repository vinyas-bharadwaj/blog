from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name
   
  def get_absolute_url(self):
      return reverse("home")
  
class Profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  bio = models.TextField(null=True, blank=True)
  profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profiles/")
  links = models.CharField(max_length=255, null=True, blank=True)
  USERNAME_FIELD = User.username


  def __str__(self):
    return str(self.user)
  
  def get_absolute_url(self):
    return reverse("home")


class Post(models.Model):
  title = models.CharField(max_length=255)
  header_img = models.ImageField(null=True, blank=True, upload_to="images/")
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = RichTextField(blank=True, null=True)
  created_at = models.DateField(auto_now_add=True)
  category = models.CharField(max_length=255, default="uncategorized")
  snippet = models.CharField(max_length=255)
  likes = models.ManyToManyField(User, related_name='blog_posts')
  
  def total_likes(self):
     return self.likes.count()

  def __str__(self) -> str:
    return self.title + " | " + str(self.author)
  
  def get_absolute_url(self):
      return reverse("posts", kwargs={"pk": self.pk})
  
class Comment(models.Model):
   post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
   name = models.CharField(max_length=255)
   body = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)

   def __str__(self) -> str:
      return f"{self.post.title} - {self.name}"

  