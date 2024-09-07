from django.urls import path
from . import views

urlpatterns = [
  path('register', views.RegistrationForm.as_view(), name='register'),
]