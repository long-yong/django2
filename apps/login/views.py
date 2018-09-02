"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.login.models import *

def init_my_info(request):
    request.session['me_name'] = ''
    request.session['me_id'] = 0

def initMySession(request):
    initSession(request, ['first_name', 'last_name', 'email', 'pwd', 'confirm', 'log_email', 'log_pwd'])

def cpyMySession(request):
    initMySession(request)
    cpySession(request, ['first_name', 'last_name', 'email', 'pwd', 'confirm'])

def cpyLogSession(request):
    initMySession(request)
    cpySession(request, ['log_email', 'log_pwd'])

def no_login(request):
    if 'me_id' not in request.session: return True
    if request.session['me_id'] == 0: return True
    return False

def no_post(request):
    if request.method != 'POST': return True
    return False

def log_out(request):
    initMySession(request)
    init_my_info(request)


#  routes

def login(request):
    if not checkPostOnce(request):
        initMySession(request)
    return render(request, "login/login.html")

def login_(request, mode):
    if no_post(request): return HttpResponse("Invalid post!")
    mode = int(mode)
    if mode == 1:
        addPostOnce(request)
        cpyMySession(request)
        errors = User.objects.reg_validator(request)
        for key, value in errors.items(): messages.error(request, value)
        return redirect('/login/login')
    if mode == 2:
        addPostOnce(request)
        cpyLogSession(request)
        errors = User.objects.log_validator(request)
        for key, value in errors.items(): messages.error(request, value)
        if len(errors):
            return redirect('/login/login')
        else:
            messages.error(request, 'Congratulate! You successfully logged in')
            return redirect('/login/login')
