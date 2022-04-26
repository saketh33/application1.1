from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model



# Create your views here

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],
                email=request.POST['email'])
                auth.login(request,user)
                return redirect('ssucess')
        else:
            return render (request,'signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('lsucess')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')


def signupsucess(request):
    return render(request, 'signupsucess.html')

def loginsucess(request):
    return render(request, 'loginsucess.html')

