from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register_show/', views.register_show, name='register_show'),
]