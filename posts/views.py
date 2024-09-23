from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

posts = [
    {
        'id': 1,
        'name': 'Aernest',
        'hobby': 'Programming'
    },
    {
        'id': 2,
        'name': 'Rahab',
        'hobby': 'Networking'
    },
    {
        'id': 3,
        'name': 'Muthiga',
        'hobby': 'Construction Management'
    }
]

def index(request:HttpRequest):
    name = request.GET.get('name') or 'World'

    context = {
        'name': name,
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

def greet(request:HttpRequest):
    name = request.GET.get('name') or 'World'
    return HttpResponse(f'Hello {name}')

def return_all_posts(request:HttpRequest):

    return HttpResponse(str(posts))

def return_one_post(request:HttpResponse, post_id):
    for post in posts:
        if post['id'] == post_id:
            return HttpResponse(str(post))
    return HttpResponse('post not found')