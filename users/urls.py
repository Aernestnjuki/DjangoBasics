from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name = 'users/login.html',
        authentication_form = UserLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]