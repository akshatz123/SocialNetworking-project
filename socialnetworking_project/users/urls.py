from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('register/', views.register_view, name='register'),
    # path('login/' views.login)
]