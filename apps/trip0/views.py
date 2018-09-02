"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.trip0.models import *

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

def initJobSession(request):
    initSession(request, ['destination', 'desc', 'date_from', 'date_to'])
    request.session['date_from'] = getTimeStr(2)
    request.session['date_to'] = getTimeStr(2)

def cpyJobSession(request):
    initJobSession(request)
    cpySession(request, ['destination', 'desc', 'date_from', 'date_to'])

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

def delete_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    for user in User.objects.all():
        if trip in user.tripss.all():
            user.tripss.remove(trip)
    trip.delete()

def cancel_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    myself = User.objects.get(id=request.session['me_id'])
    myself.tripss.remove(trip)

def join_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    myself = User.objects.get(id=request.session['me_id'])
    if trip not in myself.tripss.all():
        myself.tripss.add(trip)

#  routes

def login(request):
    if not checkPostOnce(request):
        initMySession(request)
    return render(request, "trip0/login.html")

def login_(request, mode):
    if no_post(request): return HttpResponse("Invalid post!")
    mode = int(mode)
    if mode == 1:
        addPostOnce(request)
        cpyMySession(request)
        errors = User.objects.reg_validator(request)
        for key, value in errors.items(): messages.error(request, value)
        return redirect('/trip0/login')
    if mode == 2:
        addPostOnce(request)
        cpyLogSession(request)
        errors = User.objects.log_validator(request)
        for key, value in errors.items(): messages.error(request, value)
        if len(errors): return redirect('/trip0/login')
        else: return redirect('/trip0/job_plan')


def job_plan(request):
    if no_login(request): return redirect('/trip0/login')
    myself = User.objects.get(id=request.session['me_id'])
    context = {
        'my_trips': Trip.objects.filter(planner=myself),
        'my_tripss': myself.tripss.all(),
        'all_trips': Trip.objects.all(),
    }
    return render(request, "trip0/job_plan.html", context)

def job_plan_(request, mode, id):
    if no_post(request): return HttpResponse("Invalid post!")
    mode = int(mode); id = int(id); request.session['trip_id'] = id
    if mode == 1: return redirect('/trip0/job_add')
    if mode == 2: return redirect('/trip0/login')
    if mode == 3: log_out(request); return redirect('/trip0/login')
    if mode == 4: return redirect('/trip0/job_detail')
    if mode == 5: delete_trip(request, id); return redirect('/trip0/job_plan')
    if mode == 6: cancel_trip(request, id); return redirect('/trip0/job_plan')
    if mode == 7: join_trip(request, id); return redirect('/trip0/job_plan')


def job_add(request):
    if no_login(request): return redirect('/trip0/login')
    return render(request, "trip0/job_add.html")

def job_add_(request, mode):
    if no_post(request): return HttpResponse("Invalid post!")
    mode = int(mode)
    if mode == 1:
        return redirect('/trip0/job_plan')
    elif mode == 2:
        log_out(request)
        return redirect('/trip0/login')
    elif mode == 3:
        addPostOnce(request)
        cpyJobSession(request)
        errors = Trip.objects.trip_validator(request)
        for key, value in errors.items(): messages.error(request, value)
        if len(errors): return redirect('/trip0/job_add')
        else: return redirect('/trip0/job_plan')


def job_detail(request):
    if no_login(request): return redirect('/trip0/login')
    context = {
        'this_trip': Trip.objects.get(id=request.session['trip_id']),
    }
    return render(request, "trip0/job_detail.html", context=context)

def job_detail_(request, mode):
    if no_post(request): return HttpResponse("Invalid post!")
    mode = int(mode)
    if mode == 1: return redirect('/trip0/job_plan')
    if mode == 2: log_out(request); return redirect('/trip0/login')
