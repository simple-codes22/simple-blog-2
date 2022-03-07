from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def home_page(request, *args, **kwargs):
    articles = article.objects.order_by('-date_published')
    return render(request, 'index.html', {'articles': articles})

def login_page(request, *args, **kwargs):
    if request.method == "POST":
        try:
            logged_user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, logged_user) if logged_user is not None else print('Error Logging in, logged user produced:', logged_user)
        except Exception:
            return 
        return redirect('Main:HomePage')
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
def dashboard_page(request, article_id, *args, **kwargs):
    if request.method == 'POST':
        if article_id != 'new-article':
            try:
                article.objects.filter(article_id=article_id).update(
                    title=request.POST['title'],
                    subtitle=request.POST['subtitle'],
                    summary_intro= request.POST['introduction'],
                    body=request.POST['body']
                )
                print('Article Updated Successfuly')
                return redirect('Main:HomePage')
            except Exception:
                print(Exception)
        else:
            try:
                article.objects.create(
                    owner=request.user,
                    title=request.POST['title'],
                    subtitle=request.POST['subtitle'],
                    summary_intro= request.POST['introduction'],
                    body=request.POST['body']
                )
                print('Article Created Successfuly')
                return redirect('Main:HomePage')
            except Exception:
                print(Exception)
    return render(request, 'dashboard.html', {
        'article': article_id if article_id == 'new-article' else article.objects.get(article_id=article_id)
    })

@login_required(login_url='Main:Login')
def logout_page(request, *args, **kwargs):
    logout(request)
    print(request.user)
    return redirect('Main:HomePage')

def view_page(request, article_id, *args, **kwargs):
    individual_article = article.objects.get(article_id=article_id)
    return render(request, 'view.html', {'article_detail': individual_article})

@login_required(login_url='Main:Login')
def delete_article(request, article_id, *args, **kwargs):
    try:
        article_to_delete = article.objects.get(article_id=article_id)
        article_to_delete.delete()
        return redirect('Main:HomePage')
    except Exception:
        return redirect('Main:HomePage')
