# models.py
# CMD: python manage.py makemigrations /  python manage.py migrate
from __future__ import unicode_literals
from django.db import models
from applib.yong.comfunc import *
import bcrypt

class UserManager(models.Manager):
    def hashPwd(self, pwd):
        hash = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        hash = hash.decode()
        return hash

    def checkPwd(self, pwd, hash):
        return bcrypt.checkpw(pwd.encode(), hash.encode())

    def reg_validator(self, request):
        errors = {'TITLE': 'Invalid Registration:'}
        post = request.POST
        key = 'first_name'
        if len(post[key]) < 2:
            errors[key] = "first name should be at least 2 characters"
        elif not post[key].isalpha():
            errors[key] = "first name must be alphabet"
        key = 'last_name'
        if len(post[key]) < 2:
            errors[key] = "last name should be at least 2 characters"
        elif not post[key].isalpha():
            errors[key] = "last name must be alphabet"
        key = 'email'
        err = checkEmail(post[key])
        if len(err): errors[key] = err
        elif User.objects.filter(email=post[key]).exists():
            errors[key] = 'email has existed'
        key = 'pwd'
        if len(post[key]) < 8:
            errors[key] = "password should be at least 8 characters"
        elif post[key] != post['confirm']:
            errors['confirm'] = "confirm must match password"
        if len(errors) == 1:
            errors['TITLE'] = "Congratulate! You successfully registered."
            user = User.objects.create(email='email')
            user.first_name = post['first_name']
            user.last_name = post['last_name']
            user.email = post['email']
            user.pwd = self.hashPwd(post['pwd'])
            user.save()
        return errors

    def log_validator(self, request):
        errors = {'TITLE': 'Invalid Login:'}
        post = request.POST
        email = post['log_email']
        pwd = post['log_pwd']
        if email == '':
            errors['login'] = 'please input your email and password'
        elif not User.objects.filter(email=email).exists():
            errors['login'] = 'email do not exist'
        else:
            get = User.objects.get(email=email)
            hash = get.pwd
            if not self.checkPwd(pwd, hash):
                errors['login'] = 'password is not match'
            else:
                request.session['me_name'] = get.first_name + ' ' + get.last_name
                request.session['me_id'] = get.id
                request.session['trip_id'] = 1
        if len(errors) == 1: errors = {}
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


#  -------   trip  --------

class TripManager(models.Manager):
    def trip_validator(self, request):
        errors = {'ERRORS': 'Invalid Add Operation:'}
        post = request.POST
        key = 'title'
        if len(post[key]) < 1:
            errors[key] = "Title must not be empty"
        elif len(post[key]) > 30:
            errors[key] = "Title should be no more than 30 letters"
        key = 'desc'
        if len(post[key]) < 1:
            errors[key] = "description must not be empty"
        elif len(post[key]) > 30:
            errors[key] = "description should be no more than 30 letters"
        key = 'location'
        if len(post[key]) < 1:
            errors[key] = "location must not be empty"
        elif len(post[key]) > 30:
            errors[key] = "location should be no more than 30 letters"
        if len(errors) == 1:
            errors = {}
            id = request.session['me_id']
            myself = User.objects.get(id=id)
            title = post['title']
            desc = post['desc']
            location = post['location']
            if Trip.objects.filter(planner=id, title=title, desc=desc, location=location).exists():
                pass
            else:
                trip = Trip.objects.create(planner=User.objects.get(id=id), title=title, desc=desc, location=location)
                myself.tripss.add(trip)
        return errors

    def trip_edit_validator(self, request):
        errors = {'ERRORS': 'Invalid Add Operation:'}
        post = request.POST
        key = 'title'
        if len(post[key]) < 1:
            errors[key] = "Title must not be empty"
        elif len(post[key]) > 30:
            errors[key] = "Title should be no more than 30 letters"
        key = 'desc'
        if len(post[key]) < 1:
            errors[key] = "description must not be empty"
        elif len(post[key]) > 30:
            errors[key] = "description should be no more than 30 letters"
        key = 'location'
        if len(post[key]) < 1:
            errors[key] = "location must not be empty"
        elif len(post[key]) > 30:
            errors[key] = "location should be no more than 30 letters"
        if len(errors) == 1:
            errors = {}
            trip = Trip.objects.get(id=request.session['trip_id'])
            trip.title = request.session['title']
            trip.desc = request.session['desc']
            trip.location = request.session['location']
            trip.save()
        return errors

class Trip(models.Model):
    joiners = models.ManyToManyField(User, related_name="tripss")
    planner = models.ForeignKey(User, related_name="trips", on_delete="CASCADE", default=1)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    location = models.CharField(max_length=255)
    objects = TripManager()



