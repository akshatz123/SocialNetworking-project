from django import forms
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from socialnetworking_project.settings import AUTH_USER_MODEL as user


# class Profile(models.Model):
#     """docstring for Profile"""
#     user = models.OneToOneField(user, on_delete=models.CASCADE)
class UserRegisterForm(forms.ModelForm):
    username = forms.EmailField(label= 'Email Address')
    email = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    dateofbirth = forms.DateField(label='Date of birth')

    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'dateofbirth'
        ]