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


# class Trip(models.Model):
#     joiners = models.ManyToManyField(User, related_name="tripss")
#     planner = models.ForeignKey(User, related_name="trips", on_delete="CASCADE", default=1)
#     destination = models.CharField(max_length=255)
#     desc = models.TextField()
#     date_from = models.CharField(max_length=255)
#     date_to = models.CharField(max_length=255)



