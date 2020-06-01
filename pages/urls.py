from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^index/$', pages_index),
    url(r'^detail/$', pages_detail),
    url(r'^create/$', pages_create),
    url(r'^update/$', pages_update),
    url(r'^delete/$', pages_delete),
]
