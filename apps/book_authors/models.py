from __future__ import unicode_literals
from django.db import models
# in django shell: from apps.app1.models import *
# cmd: python manage.py makemigrations
# cmd: python manage.py migrate
# one_to_many table ForeignKey tail add  ,on_delete="CASCADE")
# models field types:  https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#  Book many_many Author

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

