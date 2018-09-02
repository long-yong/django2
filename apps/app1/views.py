"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
#from apps.app1.models import *

def initMySession(request):
    initSession(request, ['name'])

def cpyMySession(request):
    initMySession(request)
    cpySession(request, ['name'])

def no_post(request):
    if request.method != 'POST': return True
    return False

#  routes

def app1(request):
    if not checkPostOnce(request):
        initMySession(request)
    return render(request, "app1/app1.html")

def app1_(request, mode):
    if no_post(request): return HttpResponse("Invalid post!")
    mode = int(mode)
    if mode == 1:
        initMySession(request)
        return redirect('/app1/app1')
    if mode == 2:
        addPostOnce(request)
        cpyMySession(request)
        return redirect('/app1/app1')
