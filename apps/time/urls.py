"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',      views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^(?P<word>\w+)$', views.no_route, name='no_route'),

]
