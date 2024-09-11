from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.RegistrationForm.as_view(), name='register'),
  path('profile/', views.UserEditForm.as_view(), name='profile'),
  #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
  path('password/', views.PasswordChangeView.as_view()),
  path('password/change/success', views.password_change_success, name='password-change-success')
]