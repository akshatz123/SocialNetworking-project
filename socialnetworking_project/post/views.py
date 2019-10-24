from django.shortcuts import render

# Create your views here.


def user_only(user):
    return user.is_authenticated
