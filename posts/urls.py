from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts-home'),
    path('greet/', views.greet, name='greet_name'),
    path('posts/', views.return_all_posts, name='all_posts'),
    path('post/<int:post_id>/', views.return_one_post, name='one_post'),
    path('about/', views.about, name='about-page'),
    path('services/', views.services, name='services-page')
]