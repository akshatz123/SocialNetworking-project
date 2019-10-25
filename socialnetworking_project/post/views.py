from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import *


def user_only(user):
    return user.is_authenticated()


@login_required(user_only, login_url='/')
def post(request):
    id = request.GET.get('id', None)
    post = Post.objects.all()
    if id is not None:
        post = get_object_or_404(Post, id=id)
    else:
        post = None
    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            post.delete()
            messages.add_message(request, messages.INFO, 'POST DELETED!')
            return HttpResponseRedirect(reverse('post.dashboard'))
