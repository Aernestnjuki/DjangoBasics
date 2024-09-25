from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request:HttpRequest):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'title': 'Home Page'
    }
    return render(request, 'index.html', context)


def about(request:HttpRequest):
    context = {
        'title': 'About page'
    }
    return render(request, 'about.html', context)

def services(request:HttpRequest):
    context = {
        'title': 'Services page'
    }
    return render(request, 'services.html', context)


@login_required
def create_post(request):
    form = PostCreationForm()

    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect('posts-home')
    context={
        'form': form
    }
    return render(request, 'create_post.html', context)

@login_required
def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)

@login_required
def update_post(request, post_id):
    post_to_update = Post.objects.get(pk=post_id)

    form = PostCreationForm(instance=post_to_update)

    if request.method == "POST":
        form = PostCreationForm(instance=post_to_update, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts-home')
    context = {
        'form': form
    }
    return render(request, 'update_post.html', context)