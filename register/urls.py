from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as v

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    url(r'^logout/$', auth_views.auth_logout, name='logout'),
    url('login/$', auth_views.auth_login, name='login'),
    path("register/", v.register, name="register"),
    url('admin/', admin.site.urls, name='admin'),

]
