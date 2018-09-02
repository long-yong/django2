"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.dojo_ninjas.models import *

# common

def show_all():
    showCls(Dojo)
    showCls(Ninjas)
    for id in range(1, 4):
        rcds = Ninjas.objects.filter(dojo=Dojo.objects.get(id=id))
        showQry(rcds)

def clear_all():
    Ninjas.objects.all().delete()
    Dojo.objects.all().delete()


# add dojo

def add_dojo(name, city, state):
    if Dojo.objects.filter(name=name, city=city, state=state).exists(): pass
    else: Dojo.objects.create(name=name, city=city, state=state)
    get = Dojo.objects.get(name=name, city=city, state=state)
    return get.id


# add ninjas

def add_ninjas(first_name, last_name, did):
    if Ninjas.objects.filter(first_name=first_name, last_name=last_name, dojo=Dojo.objects.get(id=did)).exists(): pass
    else: Ninjas.objects.create(first_name=first_name, last_name=last_name, dojo=Dojo.objects.get(id=did))
    get = Ninjas.objects.get(first_name=first_name, last_name=last_name, dojo=Dojo.objects.get(id=did))
    return get.id

# routes

def index(request):
    if checkPostOnce(request) == False :
        request.session['info1'] = ''
        request.session['info2'] = ''
    return render(request, "dojo_ninjas/index.html")

def index_post(request):
    addPostOnce(request)

    did = add_dojo("CodingDojo Silicon Valley", "Mountain View", "CA")
    add_ninjas("Ninjas", "one", did)
    add_ninjas("Ninjas", "two", did)

    did = add_dojo("CodingDojo Seattle", "Seattle", "WA")
    add_ninjas("Ninjas", "three", did)
    add_ninjas("Ninjas", "four", did)

    did = add_dojo("CodingDojo New York", "New York", "NY")
    add_ninjas("Ninjas", "five", did)
    add_ninjas("Ninjas", "six", did)

    request.session['info1'] = clsStr(Dojo)
    request.session['info2'] = clsStr(Ninjas)

    print("Dojo first:"); print(Dojo.objects.first().ninjasis.all())
    print("Dojo last:");  print(Dojo.objects.last().ninjasis.all())

    showQry(Dojo.objects.last().ninjasis.all())

    return redirect("/dojo_ninjas/index")