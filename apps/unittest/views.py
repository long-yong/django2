"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
#from apps.unittest.models import *

def initMySession(request):
    initSession(request, ['name'])

def cpyMySession(request):
    initMySession(request)
    cpySession(request, ['name'])

def no_post(request):
    if request.method != 'POST': return True
    return False

#  routes

def unittest(request):
    if not checkPostOnce(request):
        initMySession(request)
    return render(request, "unittest/unittest.html")

def unittest_(request, mode):
    if no_post(request): return HttpResponse("Invalid post!")
    mode = int(mode)
    if mode == 1:
        initMySession(request)
        return redirect('/unittest/unittest')
    if mode == 2:
        addPostOnce(request)
        cpyMySession(request)
        return redirect('/unittest/unittest')
