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
    url(r'^login_/(?P<mode>\d+)$',       views.login_,       name='login_'),

    url(r'^job_plan$',                             views.job_plan,  name='job_plan'),
    url(r'^job_plan_/(?P<mode>\d+)/(?P<id>\d+)$',  views.job_plan_, name='job_plan_'),

    url(r'^job_detail$',                 views.job_detail,   name='job_tail'),
    url(r'^job_detail_/(?P<mode>\d+)$',  views.job_detail_,  name='job_tail_'),

    url(r'^job_add$',                    views.job_add,      name='job_add'),
    url(r'^job_add_/(?P<mode>\d+)$',     views.job_add_,     name='job_add_'),

]