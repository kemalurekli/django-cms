# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=120, verbose_name ='Başlık')
    content = models.TextField(verbose_name ='İçerik')
    publishing_date = models.DateTimeField(verbose_name ='Yayınlanma Tarihi')

    def __str__(self):
        return self.title