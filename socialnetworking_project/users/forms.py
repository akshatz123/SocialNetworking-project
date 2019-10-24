from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(label= 'Email Address')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    dateofbirth = forms.DateField(label='Date of birth', widget=DateInput)

    class Meta:
        model = User
        fields =[
            'first_name',
            'last_name',
            'username',
            'dateofbirth',

        ]