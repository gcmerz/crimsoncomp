# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def __die__(self):
        self.delete(using=DEFAULT_DB_ALIAS, keep_parents=False)

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField(Contributor)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
