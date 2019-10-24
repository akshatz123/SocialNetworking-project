from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(label= 'Email Address')
    email = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    dateofbirth = forms.DateField(label='Date of birth')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'dateofbirth']