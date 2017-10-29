# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Content(models.Model):
	title = models.CharField(max_length=500)
	subtitle = models.CharField(max_length=500)
	contributors = models.ManyToManyField('Contributor', related_name = 'content')
	pub_date = models.DateTimeField('date published')

class Article(Content):
	text = models.TextField()
	def show(self):
		print self.title+"\n"+self.subtitle+"\n"+"".join(self.contributors)+"\n"+str(self.pub_date)

class Contributor(models.Model):
	first_name = models.CharField(max_length=500)
	last_name = models.CharField(max_length=500)
	def die(self):
		instance = Contributor.objects.get(id=id)
		instance.delete()
		#I couldn't quite figure this one out :(
	def show(self):
		print self.first_name
