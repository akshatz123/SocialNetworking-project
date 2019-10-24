from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from socialnetworking_project import settings


class Profile(models.Model):
    """docstring for Profile"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)