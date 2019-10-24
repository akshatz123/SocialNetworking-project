from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', ]

from django import forms

from .models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.EmailField(label= 'Email Address')
    email = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    dateofbirth = forms.DateField(label='Date of birth')

    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'dateofbirth'
        ]