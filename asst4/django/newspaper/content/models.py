# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    #def __init__(self, title, subtitle, contributors, pub_date, text):
    #   super(Article, self).__init__(title, subtitle, contributors, pub_date)
    text = models.TextField()
    def show(self):
        print "Title: %s\nSubtitle: %s\nBy: %s\nDate: %s\n%s\n" % (self.headline, self.subtitle, self.contributors, self.pub_date, self.text)


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    def die(self):
    	self.delete()