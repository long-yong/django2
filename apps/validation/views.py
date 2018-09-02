"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.validation.models import *


def clear_all():
    Blog.objects.all().delete()

def blog_id(name):
    if Blog.objects.filter(name=name).exists(): pass
    else: Blog.objects.create(name=name)
    get = Blog.objects.get(name=name)
    return get.id

def savePost(request):
    id = blog_id(request.POST['name'])
    blog = Blog.objects.get(id=id)
    blog.name = request.POST['name']
    blog.desc = request.POST['desc']
    blog.save()


# routes

def index(request):
    checkPostOnce(request)
    context = {'my_rcds': Blog.objects.all()}
    return render(request, "validation/index.html", context)

def index_err(request):
    return render(request, "validation/index_err.html")

def index_post(request):
    addPostOnce(request)
    cpySession(request, ['name','desc'])

    # showCls(Blog, ['id', 'name'])

    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/validation/index_err')
    else:
        savePost(request)

        return redirect('/validation/')

