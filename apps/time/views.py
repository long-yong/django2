"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *


def index(request):
    return render(request, "time/index.html")


def no_route(request, word):
    return HttpResponse("<h2> Route: <" + word + "> not in time.</h2>")

