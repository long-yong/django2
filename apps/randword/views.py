"""   views.py
"""

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
from applib.yong.comfunc import *


def index(request):
    checkPostOnce(request, 1)
    request.session['word'] = get_random_string(14)
    return render(request, "randword/index.html")


def index_post(request):
    addPostOnce(request)
    return redirect("/randword/index")









