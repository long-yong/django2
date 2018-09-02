"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *

def index(request):
    if checkPostOnce(request,0,True,True) == False:
        nullSessionDicts(request)
    return render(request, "session_words/index.html")

def index_post(request):
    addPostOnce(request)
    cpySession(request, ['word', 'color', 'checkbox'])
    if request.session['word'] != '':
        addSessionDicts(request, ['word', 'color', 'checkbox'], getTimeStr(1))
        resetSessionDicts(request, 'checkbox', 'on', 12)
        resetSessionDicts(request, 'checkbox',  '',  8)
        resetSessionDicts(request, 'color',     '',  'black')
    return redirect("/session_words/index")

def index_clear(request):
    clearSession(request)
    return redirect("/session_words/index")

