from __future__ import unicode_literals
from django.db import models
# in django shell: from apps.app1.models import *
# cmd: python manage.py makemigrations
# cmd: python manage.py migrate
# one_to_many table ForeignKey tail add  ,on_delete="CASCADE")
# models field types:  https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Book many_to_one Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete="CASCADE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Publisher many_to_many Book
class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

