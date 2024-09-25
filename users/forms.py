from ctypes import windll

from django import forms

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



class UserSignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))