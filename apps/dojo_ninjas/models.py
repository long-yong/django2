from __future__ import unicode_literals
from django.db import models
# in django shell: from apps.user.models import *
# cmd: python manage.py makemigrations
# cmd: python manage.py migrate
# one_to_many ForeignKey tail add  [  ,on_delete="CASCADE")  ]
# models field types:  https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types

class Dojo(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)


# Ninjas many_to_one Dojo

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjasis", on_delete="CASCADE")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

