"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',                 views.unittest,        name='unittest'),
    url(r'^index$',            views.unittest,        name='unittest'),

    url(r'^unittest$',                    views.unittest,        name='unittest'),
    url(r'^unittest_/(?P<mode>\d+)$',     views.unittest_,       name='unittest_'),

]