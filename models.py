from __future__ import unicode_literals

from django.db import models


class Content(models.Model):
	title = models.CharField(max_length=500)
	subtitle = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	contributors = models.ManyToManyField('Contributor',
                                          related_name='content')


class Article(Content):
	text = models.TextField()

	def show(self):
		print '{0} was written by {1}\n{2}\n{3}'.format(self.title, self.contributors, self.subtitle, self.pub_date)


class Contributor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def die(self):
		Model.delete(using=DEFAULT_DB_ALIAS,keep_parents=True)


# Create your models here.
