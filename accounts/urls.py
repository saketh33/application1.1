from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as a_views

urlpatterns = [
path('login/', views.login, name='login'),
path('signup/', views.signup, name='signup'),
path('signupsucess/', views.signupsucess, name='ssucess'),
path('loginsucess/', views.loginsucess, name='lsucess'),
]

