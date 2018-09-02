"""  url.py
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$',               views.index,           name='index'),
    url(r'^index$',          views.index,           name='index'),
    url(r'^register_post$',  views.register_post,   name='register_post'),
    url(r'^index_info$',     views.index_info,      name='index_info'),
    url(r'^login_post$',     views.login_post,      name='login_post'),
    url(r'^info_back$',      views.index,           name='index'),

    url(r'^board$',          views.board,            name='board'),
    url(r'^board_post_mes$', views.board_post_mes,   name='board_post_mes'),
    url(r'^board_post_com$', views.board_post_com,   name='board_post_com'),

]
