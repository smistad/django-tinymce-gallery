from django.conf.urls import url, include
from django.contrib import admin

import gallery.views

urlpatterns = [
    url(r'^browser/$', gallery.views.browser, name='browser'),
]