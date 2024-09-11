from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePassword

# Create your views here.
class RegistrationForm(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')

class UserEditForm(generic.UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/profile.html'
  success_url = reverse_lazy('home')

  def get_object(self):
    return self.request.user
  
class PasswordChangeView(PasswordChangeView):
  form_class = ChangePassword
  success_url = reverse_lazy('password-change-success')
  template_name ='registration/change-password.html'

def password_change_success(request):
  return render(request, 'registration/password_change.html', {})


