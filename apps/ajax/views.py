"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.ajax.models import *
from django.core import serializers
import json

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def my_view(request):
    return HttpResponse('Hello world')

def initMySession(request):
    initSession(request, ['first_name', 'last_name', 'email', 'age'])

def cpyMySession(request):
    initMySession(request)
    cpySession(request, ['first_name', 'last_name', 'email', 'age'])

# route

def login(request):
    if not checkPostOnce(request):
        initMySession(request)
    return render(request, "ajax/login.html")

def login_(request, mode):
    mode = int(mode)
    if mode == 1:
        return redirect('/ajax/login')
    if mode == 2:
        return redirect('/ajax/ajax')
    if mode == 3:
        addPostOnce(request)
        cpyMySession(request)
        errors = User.objects.reg_validator(request)
        for key, value in errors.items(): messages.error(request, value)
        return redirect('/ajax/login')


def ajax(request):
    return render(request, 'ajax/ajax.html')

def ajax_(request, mode):
    mode = int(mode)
    if mode == 1:
        return redirect('/ajax/login')
    if mode == 2:
        return redirect('/ajax/paging')
    if mode == 3:
        users = User.objects.filter(first_name__startswith=request.POST['name'])
        return render(request, 'ajax/partial.html', {'users': users})


def paging(request):
    return render(request, 'ajax/paging.html')

def paging_(request, mode):
    mode = int(mode)
    if mode == 1:
        return redirect('/ajax/ajax')
    if mode == 2:
        return redirect('/ajax/demo1')
    if mode == 3:
        users = User.objects.filter(first_name__startswith=request.POST['name'])
        return render(request, 'ajax/partial.html', {'users': users})
    if mode == 4:
        users = User.objects.all()
        return render(request, 'ajax/partial.html', {'users': users})


def demo1(request):
    return render(request, 'ajax/demo1.html')

def demo1_(request, mode):
    mode = int(mode)
    print(mode)
    if mode == 1:
        return redirect('/ajax/paging')
    if mode == 2:
        return redirect('/ajax/demo2')
    if mode == 3:
        users = User.objects.all()
        return HttpResponse(serializers.serialize("json", users), content_type='application/json')
    if mode == 4:
        return render(request, 'ajax/partial.html', {"users": User.objects.all()})


def demo2(request):
    return render(request, 'ajax/demo2.html')

def demo2_(request, mode):
    mode = int(mode)
    if mode == 1:
        return redirect('/ajax/demo1')
    if mode == 2:
        return redirect('/ajax/demo3')
    if mode == 3:
        return render(request, 'ajax/partial.html', {"users": User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])})


def demo3(request):
    return render(request, 'ajax/demo3.html')

def demo3_(request, mode):
    mode = int(mode)
    if mode == 1:
        return redirect('/ajax/demo2')
    if mode == 2:
        return redirect('/ajax/demo3')
    if mode == 3:
        return render(request, 'ajax/partial.html', {"users": User.objects.order_by("-id")})
