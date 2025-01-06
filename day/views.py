from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods


def create(request):
    return render(request, 'create.html')


def store(request):
    name = request.POST.get('name')
    age = request.POST.get('age')

