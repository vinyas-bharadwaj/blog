from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from app.models import Profile

class SignUpForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

  def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs ['class'] = 'form-control'

class EditSettingsForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name']

    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
    }

class CreateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio', 'profile_pic', 'links']

    widgets = {
      'bio': forms.TextInput(attrs={'class': 'form-control'}),
      'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
      'links': forms.TextInput(attrs={'class': 'form-control'}),
    }

class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio', 'profile_pic', 'links']

    widgets = {
      'bio': forms.TextInput(attrs={'class': 'form-control'}),
      'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
      'links': forms.TextInput(attrs={'class': 'form-control'}),
    }

class ChangePassword(PasswordChangeForm):
  old_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
  new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

  class Meta:
    model = User
    fields = ['old_password', 'new_password1', 'new_password2']
   


