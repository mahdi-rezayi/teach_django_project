from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def create(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'article/create.html', context)


def store(request):
    title = request.POST.get('title')
    description = request.POST.get('description')

    Article.objects.create(title=title, content=description)
    return redirect('index')

