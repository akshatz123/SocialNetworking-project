from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import get_user_model
User = get_user_model()
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # path('login/', views.login, name='login'),
]