from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
# from socialnetworking_project.settings import LOGIN_REDIRECT_URL
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('register/', views.register_view, name='register'),

]