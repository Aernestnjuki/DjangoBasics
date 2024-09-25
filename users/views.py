from django.shortcuts import render, redirect
from .forms import UserSignUpForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def sign_up(request):
    form = UserSignUpForm()

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            new_user = User.objects.create_user(
                username=username,
                email=email,
            )
            new_user.set_password(password)

            new_user.save()

        return redirect('posts-home')
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
