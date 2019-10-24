from django import forms
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from socialnetworking_project.settings import AUTH_USER_MODEL as user


# class Profile(models.Model):
#     """docstring for Profile"""
#     user = models.OneToOneField(user, on_delete=models.CASCADE)
class UserRegisterForm(models.Model):
    username = models.EmailField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dateofbirth = models.DateTimeField()

