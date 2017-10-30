# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Content(models.Model):
	title = models.CharField(max_length=500)
	subtitle = models.CharField(max_length=500)
	contributors = models.ManyToManyField('Contributor', related_name = 'content')
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return "%s %s %s %s" % (self.title, self.subtitle, self.contributors, str(self.pub_date))

class Article(Content):
	text = models.TextField()
	def __str__(self):
		return "%s %s %s %s %s" % (self.title, self.subtitle, self.text, self.contributors, str(self.pub_date))

class Contributor(models.Model):
	first_name = models.CharField(max_length=500)
	last_name = models.CharField(max_length=500)
	def die(self):
		self.delete()
	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)
