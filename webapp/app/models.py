from django.db import models
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
   bio = models.TextField()
   profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profiles/")
   links = models.CharField(max_length=255, null=True, blank=True)

   def __str__(self):
      return str(self.user)


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
  