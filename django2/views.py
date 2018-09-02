"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *


def index(request):
    return redirect("/ajax/index")


def page1(request):
    return HttpResponse("<h2>main.page1</h2>")

def page2(request):
    return HttpResponse("<h2>main.page2</h2>")

def year_2000(request):
    return HttpResponse("<h2>main.year_2000</h2>")

def year(request, year):
    return HttpResponse("<h2>main.year " + year + "</h2>")

def year_month(request, year, month):
    return HttpResponse("<h2>main.year_month " + year + " " + month + "</h2>")

def number(request, number):
    return HttpResponse("<h2>main.number " + number + "</h2>")

def no_route(request, word):
    return HttpResponse("<h2> Route: <" + word + "> not in main.</h2>")


