from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import date

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
	text = models.TextField(null = True)


class Contributor(models.Model):
	first_name = models.CharField(max_length = 250, null = True)
	last_name = models.CharField(max_length = 250, null = True)

	def die(self):
		self.delete()