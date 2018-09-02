from __future__ import unicode_literals
from django.db import models
# in django shell: from apps.user.models import *
# cmd: python manage.py makemigrations
# cmd: python manage.py migrate
# one_to_many ForeignKey tail add  [  ,on_delete="CASCADE")  ]
# models field types:  https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete="CASCADE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete="CASCADE")
    message = models.ForeignKey(Message, on_delete="CASCADE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#  One to one
#  this is makes an imaginary property IN THE OBJECT THAT THE ONE_TO_ONE relationship is not defined in,
#  in addition to the real property in the object that the relationship IS defined in.
#  So if we had a one_to_one relationship in an object e.g.
#  class User(models.Model):
#    first_name = models.CharField(max_length=45)
#  class CustomUserId(models.Model):
#    newId = models.IntegerField()
#    specificUser = models.OneToOneField(User)
#
#   Here a userObject has a customUserId as well as a customUserId having a specificuser property.
#   If we want to change the way we reference that artificially generated key,
#   we could change our model like this:
#
#   class User(models.Model):
#     first_name = models.CharField(max_length=45)
#   class CustomUserId(models.Model):
#     newId = models.IntegerField()
#     specificUser = models.OneToOneField(User, related_name="myId")

