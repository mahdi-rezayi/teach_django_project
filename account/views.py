from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def show_register(request):
    return render(request, 'account/register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords must match')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')

        user = User.objects.create_user(username=username, email=email, password=password2)
        login(request, user)
        # redirect code


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect code

        else:
            messages.error(request, 'Invalid username or password')


def logout_user(request):
    logout(request)
    # redirect code