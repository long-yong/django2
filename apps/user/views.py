"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.user.models import *

# common

def show_all():
    showCls(User,    ['id', 'first_name'])
    showCls(Message, ['id', 'message'])
    showCls(Comment, ['id', 'comment'])

def clear_all():
    Comment.objects.all().delete()
    Message.objects.all().delete()
    User.objects.all().delete()

# add user

def add_user(first_name, last_name='', email='', age='', password=''):
    if User.objects.filter(first_name=first_name, last_name=last_name).exists(): pass
    else: User.objects.create(first_name=first_name, last_name=last_name, email=email, age=age, password=password)
    get = User.objects.get(first_name=first_name, last_name=last_name)
    return get.id

# add message

def add_message(message, uid):
    if Message.objects.filter(message=message, user=User.objects.get(id=uid)).exists(): pass
    else: Message.objects.create(message=message, user=User.objects.get(id=uid))
    get = Message.objects.get(message=message, user=User.objects.get(id=uid))
    return get.id

def show_user_message(first_name,last_name):
    uid = add_user(first_name,last_name)
    rcds = Message.objects.filter(user=User.objects.get(id=uid))
    showRcds(rcds)

# add comment

def add_comment(comment, uid, mid):
    if Comment.objects.filter(comment=comment, user=User.objects.get(id=uid), message=Message.objects.get(id=mid)).exists(): pass
    else: Comment.objects.create(comment=comment, user=User.objects.get(id=uid), message=Message.objects.get(id=mid))
    get = Comment.objects.get(comment=comment, user=User.objects.get(id=uid), message=Message.objects.get(id=mid))
    return get.id

# routes


def index(request):
    checkPostOnce(request)
    context = {
        'all_user':     User.objects.all(),
        'all_message':  Message.objects.all(),
        'all_comment':  Comment.objects.all()
    }
    return render(request, "user/index.html", context)


def index_post(request):
    addPostOnce(request)

    uid = add_user('yong', 'long', '6527', '50')
    mid = add_message('Hi, I am yong', uid)
    add_message('How are you, Ping? I am yong', uid)

    uid = add_user('ping', 'li', '6527', '45')
    add_comment('comment yong from ping', uid, mid)
    add_comment('you looks good, from ping', uid, mid)

    showQry(User.objects.first().messages.all(), ['id', 'message'])
    for user in User.objects.all(): showQry(user.messages.all(), ['id', 'message'])

    return redirect("/user/index")