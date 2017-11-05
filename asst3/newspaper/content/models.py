# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# generic content class to develop types of content from
class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField(  'Contributor',
                                            related_name='content')
    pub_date = models.DateTimeField('date published')

class Article(Content):
    text = models.TextField()

    # allow the article to be represented by a string
    def show(self):
        return str(text)

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    # delete the contributor from the database
    def die(self):
        return self.delete()
