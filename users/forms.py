from django import forms
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

"""
class UserSignUpForm:
    username
    email
    password
    confirm

class UserLoginForm:
    username
    password
"""



# class UserSignUpForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self). __init__(*args, **kwargs)
        self.fields['username'].label = 'Enter your name'
        self.fields['username'].widget=forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].label = 'Enter your email'
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password1'].label = 'Enter your password'
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].label = 'Confirm your password'
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

# class UserLoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Enter your name'
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].label = 'Enter your password'
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'password1']