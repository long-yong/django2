"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',                        views.app1,        name='app1'),
    url(r'^index$',                   views.app1,        name='app1'),

    url(r'^app1$',                    views.app1,        name='app1'),
    url(r'^app1_/(?P<mode>\d+)$',     views.app1_,       name='app1_'),

]