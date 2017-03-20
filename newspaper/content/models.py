from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Content(models.Model):
	title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
	# Used: https://docs.djangoproject.com/en/1.10/ref/models/fields/
    text = models.TextField()


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def die(self):
          Model.delete(using=DEFAULT_DB_ALIAS, keep_parents=True)

class Image(Content):
	caption = models.CharField(max_length=500)
	path = models.CharField(max_length=500)