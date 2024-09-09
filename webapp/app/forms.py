from django import forms
from django.contrib.auth.models import User
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')


class CreatePost(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'author', 'category', 'body']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
      'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }

class EditPost(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'body']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
    }