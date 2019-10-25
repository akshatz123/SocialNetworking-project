from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def home_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        auth = authenticate(username=username, password=password)
        if auth is not None:
            login(request, auth)
            return HttpResponseRedirect('dashboard/')
        else:
            messages.add_message(request, messages.INFO, "Authentication Failed!")
            return HttpResponseRedirect('/')

    return render(request, 'home.html')


def logout_view(request):
    return render(request, 'home.html')

