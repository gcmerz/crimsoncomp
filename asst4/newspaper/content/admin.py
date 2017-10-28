# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from content.models import Content
from content.models import Contributor

admin.site.register(Content)
admin.site.register(Contributor)