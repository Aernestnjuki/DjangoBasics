from django.shortcuts import render, redirect
from .forms import UserSignUpForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

def sign_up(request):
    form = UserSignUpForm()

    if request.method == "POST":
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'User created successfully')
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def login_user(request):
    form = UserLoginForm()

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts-home')
        else:
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('signup')
