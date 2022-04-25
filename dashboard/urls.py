from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as a_views

urlpatterns = [
path('', views.index, name='index'),
path('logout', views.logout, name='logout'),
]

