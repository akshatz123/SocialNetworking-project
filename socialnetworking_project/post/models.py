from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    dateofbirth = models.DateField(auto_now=False, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Post(models.Model):
    likes = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(blank=True)

