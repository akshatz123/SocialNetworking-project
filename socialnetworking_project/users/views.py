from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # print (form)

        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            msg = 'Your account is created ! You are now able to login'
            messages.success(request, msg)
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
