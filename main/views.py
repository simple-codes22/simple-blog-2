from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def home_page(request, *args, **kwargs):
    articles = article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def login_page(request, *args, **kwargs):
    if request.method == "POST":
        try:
            logged_user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, logged_user) if logged_user is not None else print('Error Logging in, logged user produced:', logged_user)
        except Exception:
            return 
        return redirect('Main:Dashboard')
    return render(request, 'login.html')

def register_page(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            User.objects.create_user(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['e_mail'],
                password=request.POST['password'],
            )
            logged_user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, logged_user) if logged_user is not None else print('Error Logging in, logged user produced:', logged_user)
            return redirect('Main:Dashboard')
        except Exception:
            print('Error Occured')
            return redirect('Main:Homepage')
    return render(request, 'register.html')

@login_required(login_url='Main:Login')
def dashboard_page(request, *args, **kwargs):
    return render(request, 'dashboard.html')

@login_required(login_url='Main:Login')
def logout_page(request, *args, **kwargs):
    logout(request)
    print(request.user)
    return redirect('Main:HomePage')

def view_page(request, *args, **kwargs):
    return render(request, 'view.html')
