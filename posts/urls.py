from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts-home'),
    path('about/', views.about, name='about-page'),
    path('services/', views.services, name='services-page'),
    path('create_post/', views.create_post, name='create-post'),
    path('post/<int:post_id>', views.post_details, name='post-details'),
    path('post/update/<int:post_id>', views.update_post, name='update-post')
]