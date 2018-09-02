"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *


def index(request):
    checkPostOnce(request)
    return render(request, "blogs/index.html")


def index_post(request):
    addPostOnce(request)
    cpySession(request, ['name','desc'])
    return redirect("/blogs/index_post_res")


def index_post_res(request):
    return render(request, "blogs/index_post_res.html")


