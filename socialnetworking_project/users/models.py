from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from socialnetworking_project.settings import AUTH_USER_MODEL as user


class Profile(models.Model):
    """docstring for Profile"""
    user = models.OneToOneField(user, on_delete=models.CASCADE)
