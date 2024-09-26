from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='posts-home'),
    path('class-based-view', views.HomePageView.as_view(), name='home-class-view'),
    path('about/', views.ABoutPageView.as_view(), name='about-page'),
    path('services/', views.services, name='services-page'),
    path('create_post/', login_required(views.CreatePostView.as_view()), name='create-post'),
    path('post/<int:post_id>', views.post_details, name='post-details'),
    path('post/update/<int:post_id>', views.update_post, name='update-post')
]