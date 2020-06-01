# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def pages_index(request):
    return HttpResponse ('Burası index sayfası')

def pages_detail(request):
    return HttpResponse ('Burası detail sayfası')

def pages_create(request):
    return HttpResponse ('Burası create sayfası')

def pages_update(request):
    return HttpResponse ('Burası update sayfası')

def pages_delete(request):
    return HttpResponse ('Burası delete sayfası')