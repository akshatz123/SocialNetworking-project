from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
from django.db import models


class UserRegisterForm(UserCreationForm):
    username = models.EmailField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dateofbirth = models.DateTimeField()

