from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditSettingsForm, ChangePassword, EditProfileForm
from app.models import Profile, Post


# Create your views here.
class RegistrationForm(generic.CreateView):
  form_class = SignUpForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')

class UserEditForm(generic.UpdateView):
  form_class = EditSettingsForm
  template_name = 'registration/profile.html'
  success_url = reverse_lazy('home')

  def get_object(self):
    return self.request.user
  
class ProfilePageView(generic.DetailView):
  model = Profile
  template_name = 'registration/user-profile.html'

  def get_context_data(self, *args, **kwargs):
    context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

    page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
    user_posts = Post.objects.all().filter(author=page_user.user.id)

    context['page_user'] = page_user
    context['user_posts'] = user_posts
    return context
  
class EditProfilePageView(generic.UpdateView):
  form_class = EditProfileForm
  template_name = 'registration/edit-profile.html'
  success_url = reverse_lazy('home')

  def get_object(self):
    return self.request.user

  
class PasswordChangeView(PasswordChangeView):
  form_class = ChangePassword
  success_url = reverse_lazy('password-change-success')
  template_name ='registration/change-password.html'

def password_change_success(request):
  return render(request, 'registration/password_change.html', {})


