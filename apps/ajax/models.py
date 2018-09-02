# models.py
# CMD: python manage.py makemigrations /  python manage.py migrate
from __future__ import unicode_literals
from django.db import models
from applib.yong.comfunc import *
import bcrypt

class UserManager(models.Manager):

    def reg_validator(self, request):
        errors = {'TITLE': 'Invalid Registration:'}
        post = request.POST
        key = 'first_name'
        if len(post[key]) < 2:
            errors[key] = "first name should be at least 2 characters"
        key = 'last_name'
        if len(post[key]) < 2:
            errors[key] = "last name should be at least 2 characters"
        key = 'email'
        err = checkEmail(post[key])
        if len(err): errors[key] = err
        elif User.objects.filter(email=post[key]).exists():
            errors[key] = 'email has existed'
        key = 'age'
        if len(post[key]) < 1:
            errors[key] = "age should be at empty"
        elif not post[key].isdigit():
            errors[key] = "age should be a digit"
        if len(errors) == 1:
            errors['TITLE'] = "Congratulate! You successfully registered."
            user = User.objects.create(email='email')
            user.first_name = post['first_name']
            user.last_name = post['last_name']
            user.email = post['email']
            user.age = int(post['age'])
            user.save()
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



