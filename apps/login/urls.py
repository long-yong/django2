"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',                           views.login,        name='login'),
    url(r'^index$',                      views.login,        name='login'),

    url(r'^login$',                      views.login,        name='login'),
    url(r'^login_/(?P<mode>\d+)$',     views.login_,         name='login_'),

]