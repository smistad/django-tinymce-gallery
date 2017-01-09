from django.conf.urls import url, include

import testapp.views

urlpatterns = [
    url(r'^$', testapp.views.index, name='index'),
]