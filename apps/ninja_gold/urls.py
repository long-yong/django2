"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',       views.index,  name='index'),
    url(r'^index$',  views.index,  name='index'),
    url('^(?P<n0>[0-9]{1,3})/(?P<n1>[0-9]{1,3})/(?P<name>\w+)$', views.index_post, name='index_post'),
]
