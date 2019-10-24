from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('login/', views.login, name='login'),
]