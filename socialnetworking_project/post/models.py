from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
<<<<<<< HEAD
    dateofbirth = models.DateField(auto_now=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
=======
    dateofbirth = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def ___str__(self):
        return self.email
>>>>>>> 9618242319c7f51fdbcf5a987557c23d2ffab8da
