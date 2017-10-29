# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Content(models.Model):
	title = models.CharField(max_length=500)
	subtitle = models.CharField(max_length=500)
	contributors = models.ManyToManyField('Contributor', related_name='content')
	pub_date = models.DateTimeField('date published')

class Article(Content):
	text = models.TextField()
	def show(self):
		print self.title
		print self.subtitle
		for i in range(0,len(self.contributors.all())):
			self.contributors.all()[i].show()
		print self.pub_date
		print self.text

class Contributor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	def die(self):
		self.delete()
	def show(self):
		print self.first_name,
		print self.last_name
