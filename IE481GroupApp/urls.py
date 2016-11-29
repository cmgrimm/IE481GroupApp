"""
Definition of urls for IE481GroupApp.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
include('django_messages.urls')

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    (r'^messages/', include('django_messages.urls')),
    url(r'^classPage$', app.views.classPage, name='classPage'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',app.views.login,name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^recovery$', app.views.recovery, name = 'recovery'),
    url(r'^profile$', app.views.profile, name = 'profile'),
    url(r'^newaccount$', app.views.newaccount, name = 'newaccount'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
