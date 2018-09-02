"""
Django2 add a newapp process
1. Clone app1 dir to newapp, chg < 2 > app1 dir to newapp,  chg < 1 > app1.htm file to newapp
2. settings < 1 > add newapp
3. django.urls  < 1*2 > add  newapp
4. django.views < 1 > app1 chg to newapp
5. newapp.views app1 ctrl+r to newapp
6. newapp html app1 ctrl+r to newapp
7. modify newapp models.py ,  delete newapp/migrations/0000_auto.py & db.sqlite
8. CMD: python manage.py makemigrations /  python manage.py migrate
9. RUN manage.py

10. no such table:django_session error SOLOVED METHOD: python manage.py migrate
11. {% csrf_token %} must put into form's inner top, otherwise submit cause error
12. redirect use the whole path avoid wrong route

Semi-Restful Users
Bcrypt
Security Lession
Login and Registration

one         validation
one_many:   dojo_ninjas  user
many_many:  book_authors  books

(djangoPy3Env) pip install bcrypt


"""

#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
