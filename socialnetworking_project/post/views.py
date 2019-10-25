from django.http import request
from django.shortcuts import render

from django.contrib.auth import get_user_model
User = get_user_model()


def user_only(user):
    return user.is_authenticated()
