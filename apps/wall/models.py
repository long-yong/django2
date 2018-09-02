# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
from applib.yong.comfunc import *
import bcrypt
# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!!
# (just parts, like request.POST)



class UserManager(models.Manager):
    def hashPwd(self, pwd):
        hash = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        hash = hash.decode()
        return hash

    def reg_validator(self, postData):
        errors = {}
        key = 'first_name'
        if len(postData[key]) < 2:
            errors[key] = "first_name should be at least 2 characters"
        elif not postData[key].isalpha():
            errors[key] = "first_name must be alphabet"
        key = 'last_name'
        if len(postData[key]) < 2:
            errors[key] = "last_name should be at least 2 characters"
        elif not postData[key].isalpha():
            errors[key] = "last_name must be alphabet"
        key = 'email'
        err = checkEmail(postData[key])
        if err != '':
            errors[key] = err
        elif User.objects.filter(email=postData[key]).exists():
            errors[key] = 'the email has existed '
        key = 'pwd'
        if len(postData[key]) < 8:
            errors[key] = "password should be at least 8 characters"
        elif postData[key] != postData['confirm']:
            errors['confirm'] = "confirm must match password"
        return errors

    def log_validator(self, postData, myInfo):
        errors = {}
        email = postData['log_email']
        pwd = postData['log_pwd']
        if email == '':
            errors['login'] = 'please input your email and password'
        elif not User.objects.filter(email=email).exists():
            errors['login'] = 'email do not exist'
        else:
            get = User.objects.get(email=email)
            hash = get.pwd
            myInfo[0] = get.first_name+" "+get.last_name
            myInfo[1] = get.id
            if not bcrypt.checkpw(pwd.encode(), hash.encode()):
                errors['login'] = 'password is not match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

#  Message many_one User
class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete="CASCADE")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Comment many_one User
# Comment many_one Message
class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete="CASCADE")
    message = models.ForeignKey(Message, related_name="commentss", on_delete="CASCADE")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)