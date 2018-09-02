"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from random import randint

def add_gold(request, n0, n1, name):
    rs = request.session
    old = int(rs['gold'])
    n0 = int(n0)
    n1 = int(n1)
    if n1 == 50: n0 = -50
    earn = randint(n0, n1)
    if old + earn < 0: earn = -old
    rs['gold'] = str(old + earn)
    if (earn >= 0): addstr = 'Earns ' + str(earn) + ' gold from the ' + name
    else: addstr = 'Entered a casino and lost ' + str(-earn) + ' gold ... Ouch.'
    timestr =' (' + time.strftime("%Y/%m/%d %I:%M %p", time.localtime()) + ')'
    rs['activities'] = addstr + timestr + '\r\n' + rs['activities']


def index(request):
    rs = request.session
    if not checkPostOnce(request):
        rs['gold'] = '0'
        rs['activities'] = ''
    return render(request, "ninja_gold/index.html")


def index_post(request, n0, n1, name):
    if request.method == 'POST':
        addPostOnce(request)
        add_gold(request, n0, n1, name)
    return redirect("/ninja_gold/index")
