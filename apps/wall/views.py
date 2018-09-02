"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.wall.models import *

myInfo = ['No name', 1, 2]

def initMySession(request):
    initSession(request, ['first_name', 'last_name', 'email', 'pwd', 'confirm', 'log_email', 'log_pwd'])

def cpyMySession(request):
    initMySession(request)
    cpySession(request, ['first_name', 'last_name', 'email', 'pwd', 'confirm'])

def cpyLogSession(request):
    initMySession(request)
    cpySession(request, ['log_email', 'log_pwd'])

def savePost(request):
    rp = request.POST
    email = rp['email']
    if User.objects.filter(email=email).exists(): pass
    else: User.objects.create(email=email)
    get = User.objects.get(email=email)
    get.first_name = rp['first_name']
    get.last_name = rp['last_name']
    get.email = rp['email']
    get.pwd = User.objects.hashPwd(rp['pwd'])
    get.save()


# routes

def index(request):
    if not checkPostOnce(request):
        initMySession(request)
    return render(request, "wall/index.html")

def index_info(request):
    context = {
        'all_register': User.objects.all(),
    }
    return render(request, "wall/index_info.html", context)

def register_post(request):
    addPostOnce(request)
    cpyMySession(request)
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        messages.error(request, "Invalid Registration:")
        for key, value in errors.items():
            messages.error(request, value)
    else:
        savePost(request)
        messages.success(request, "Congratulate! You successfully registered.")
    return redirect('/wall/index_info')

def login_post(request):
    addPostOnce(request)
    cpyLogSession(request)
    errors = User.objects.log_validator(request.POST, myInfo)
    if len(errors):
        messages.error(request, "Invalid Login:")
        for key, value in errors.items():
            messages.error(request, value)
    else:
        messages.success(request, "Congratulate! You successfully logged in.")
    # return redirect('/wall/index_info')
    return redirect('/wall/board')

#


# ------------   wall board   ------------

def initBoardSession(request):
    initSession(request, ['message', 'comment', 'name'])

def cpyMesSession(request):
    initMySession(request)
    cpySession(request, ['message'])

def cpyComSession(request):
    initMySession(request)
    cpySession(request, ['comment'])

def showMe():
    print(myInfo[0], myInfo[1])

def show_comment_name_val(request):
    for key in request.POST:
        print(key, request.POST[key])

def board(request):
    if not checkPostOnce(request):
        initBoardSession(request)
    context = {
        'me_name': myInfo[0],
        'me_id': myInfo[1],
        'all_message':  {},
        'all_comment':  {},
    }
    showMe()
    return render(request, "wall/board.html", context)

def board_post_mes(request):
    addPostOnce(request)
    cpyMesSession(request)
    return redirect('/wall/board')

def board_post_com(request):
    addPostOnce(request)
    cpyComSession(request)
    show_comment_name_val(request)
    return redirect('/wall/board')
