"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',       views.login,     name='login'),
    url(r'^index$',  views.login,     name='login'),

    url(r'^login$',                    views.login,        name='login'),
    url(r'^login_/(?P<mode>\d+)$',     views.login_,       name='login_'),

    url(r'^ajax$',                  views.ajax,    name='ajax'),
    url(r'^ajax_/(?P<mode>\d+)$',   views.ajax_,   name='ajax_'),

    url(r'^paging$',                views.paging,   name='paging'),
    url(r'^paging_/(?P<mode>\d+)$', views.paging_,  name='paging_'),

    url(r'^demo1$',                 views.demo1,   name='demo1'),
    url(r'^demo1_/(?P<mode>\d+)$',  views.demo1_,  name='demo1_'),

    url(r'^demo2$',                 views.demo2,   name='demo2'),
    url(r'^demo2_/(?P<mode>\d+)$',  views.demo2_,  name='demo2_'),

    url(r'^demo3$',                 views.demo3,   name='demo3'),
    url(r'^demo3_/(?P<mode>\d+)$',  views.demo3_,  name='demo3_'),

]