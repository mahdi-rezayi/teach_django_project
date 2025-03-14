from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register_show/', views.show_register, name='register_show'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]