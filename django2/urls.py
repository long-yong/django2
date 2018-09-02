"""
  url.py

https://docs.djangoproject.com/en/2.1/topics/http/urls/
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'^' Matches the following characters at the beginning of a string. Example: '^a' matches 'anna' but not 'banana'.
'$' Matches the previous characters at the end of a string. Example: 'a$' matches 'anna' and 'banana' but not 'fan'.
'[]' Matches any value in a range. Example: '[0-9]' matches '9' and '9s'.
'{n}' Matches n number repetitions of the preceding pattern. Example: '[0-9]{2}' matches '91' but not '9'
\d Matches digits.  Example: "\d" matches "8" and "877"
\d+ matches a string with one or more digits
\w Matches characters.
\w+ matches a string with one or more character/word
url(r'^articles/(?P\d+)$', views.show)
url(r'^articles/(?P\w+)$', views.show_word)
url(r'^articles/2003/)$', views.special_case_2003)
url(r'^articles/(?P[0-9]{4})$', views.year_archive)
url(r'^articles/(?P[0-9]{4})/(?P[0-9]{2})$', views.month_archive)
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^app1/', include('apps.app1.urls')),
    url(r'^app1', include('apps.app1.urls')),
    url(r'^blogs/', include('apps.blogs.urls')),
    url(r'^time/', include('apps.time.urls')),
    url(r'^randword/', include('apps.randword.urls')),
    url(r'^surveys/', include('apps.surveys.urls')),
    url(r'^session_words/', include('apps.session_words.urls')),
    url(r'^ninja_gold/', include('apps.ninja_gold.urls')),
    url(r'^books/', include('apps.books.urls')),
    url(r'^user/', include('apps.user.urls')),
    url(r'^dojo_ninjas/', include('apps.dojo_ninjas.urls')),
    url(r'^book_authors/', include('apps.book_authors.urls')),
    url(r'^validation/', include('apps.validation.urls')),
    url(r'^login/', include('apps.login.urls')),
    url(r'^ajax/', include('apps.ajax.urls')),
    url(r'^wall/', include('apps.wall.urls')),
    url(r'^trip0/', include('apps.trip0.urls')),
    url(r'^trip/', include('apps.trip.urls')),
    url(r'^upload/', include('apps.upload.urls')),
    url(r'^unittest/', include('apps.unittest.urls')),


    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^page1$', views.page1, name='page1'),
    url(r'^page2$', views.page2, name='page2'),

    url(r'^2000$', views.year_2000, name='year_2000'),
    url('^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.year_month, name='year_month'),
    url('^(?P<year>[0-9]{4})$', views.year, name='year'),
    url(r'^(?P<number>\d+)$', views.number, name='number'),
    url(r'^(?P<word>\w+)$', views.no_route, name='no_route'),

]
