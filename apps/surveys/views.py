"""   views.py
"""

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *

def index(request):
    checkPostOnce(request)
    return render(request, "surveys/index.html")


def index_post(request):
    addPostOnce(request)
    cpySession(request, ['name', 'location', 'lang', 'comment'])
    return redirect("/surveys/index_post_res")


def index_post_res(request):
    return render(request, "surveys/index_post_res.html")


def index_res_back(request):
    setPostOnce(request)
    return redirect("/surveys/index")




