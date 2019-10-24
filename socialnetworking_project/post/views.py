from django.http import request
from django.shortcuts import render

# Create your views here.


def user_only(user):
    return user.is_authenticated()


def login(user):
    if user.is_authenticated():
        return render(request, 'dashboard.html')
    else:
        pass
