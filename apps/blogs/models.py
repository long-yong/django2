from __future__ import unicode_literals
from django.db import models
# in django shell: from apps.app1.models import *
# python manage.py makemigrations   python manage.py migrate
# models field types:  https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types

class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.desc)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Notice the association made with ForeignKey for a one-to-many relationship
    # There can be many comments to one blog
    blog = models.ForeignKey(Blog, related_name = "comments", on_delete="CASCADE")
class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name = "admins")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)