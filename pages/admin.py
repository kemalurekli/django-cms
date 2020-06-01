# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Pages


class Pagesadmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date']
    list_display_links =['title','publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    class Meta :
        model = Pages


admin.site.register(Pages, Pagesadmin)