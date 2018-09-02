"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def upload_file(request):
    myFile = request.FILES.get("file", None)
    if not myFile:
        messages.error(request, 'No file uploaded!')
        return False
    destination = open("C:\\Users\\longy\\Downloads\\"+myFile.name, 'wb+')
    for chunk in myFile.chunks():
        destination.write(chunk)
    destination.close()
    messages.error(request, myFile.name + ' uploaded over!')
    return True

#  routes

def upload(request):
    return render(request, "upload/upload.html")

def upload_(request, mode):
    mode = int(mode)
    if mode == 1:
        return redirect('/upload/upload')
    if mode == 2:
        upload_file(request)
        return redirect('/upload/upload')

