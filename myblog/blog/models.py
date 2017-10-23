# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model): #says Post is a Model
	title = models.CharField(max_length=500) #title with max 500 characters
	content = models.TextField() #longer
	def show(self):
		print self.title
		print self.content