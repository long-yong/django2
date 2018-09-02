"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',               views.index,          name='index'),
    url(r'^index$',          views.index,          name='index'),
    url(r'^index_post$',     views.index_post,     name='index_post'),
    url(r'^index_post_res$', views.index_post_res, name='index_post_res'),

]
