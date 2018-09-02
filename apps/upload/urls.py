"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',                        views.upload,        name='upload'),
    url(r'^index$',                   views.upload,        name='upload'),

    url(r'^upload$',                    views.upload,        name='upload'),
    url(r'^upload_/(?P<mode>\d+)$',     views.upload_,       name='upload_'),

]