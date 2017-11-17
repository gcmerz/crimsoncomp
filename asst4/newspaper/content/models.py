# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    #text = models.TextField()
    text = tinymce_models.HTMLField()
    def show(self):
        print(self.title)
        print(self.subtitle)
        print(self.contributors) 
        print(self.text)
        print(self.pub_date)

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    def die(self):
        self.delete(using=DEFAULT_DB_ALIAS, keep_parents=False)
