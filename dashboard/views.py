from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')