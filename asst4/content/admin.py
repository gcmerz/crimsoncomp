# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article, Contributor

# Register your models here.

admin.site.register(Contributor)

admin.site.register(Article)


