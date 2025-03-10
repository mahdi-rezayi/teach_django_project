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
    return render(request, 'article/create.html')


def store(request):
    title = request.POST.get('title')
    description = request.POST.get('description')

    Article.objects.create(title=title, content=description)
    return redirect('index')


def edit(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article,
    }
    return render(request, 'article/edit.html', context)


def update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('index')


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('index')
