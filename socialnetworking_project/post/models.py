from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    dateofbirth = models.DateField(auto_now=False, null=True, blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=30, unique=True)
    # last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    # is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


# class GuestEmail(models.Model):
#     email = models.EmailField()
#     active = models.BooleanField(default=True)
#     update = models.DateTimeField(auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def ___str__(self):
#         return self.email
