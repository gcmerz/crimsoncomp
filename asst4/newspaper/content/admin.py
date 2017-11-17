# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Content, Article

admin.site.register(Content)
admin.site.register(Article)
# Register your models here.
