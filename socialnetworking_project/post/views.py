from django.shortcuts import render

# Create your views here.


def user_only(user):


    if user is not None:
        login(request, user)
    else:
        pass
    return user.is_authenticated