from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from PIL import Image


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published', default=timezone.now)


class Article(Content):
    text = models.TextField()
    headline = models.CharField(max_length=200)


class Image(Content):
    caption = models.CharField(max_length=200)
    path = models.CharField(max_length=200)


class Contributor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    def die(self):
      Model.delete(using=DEFAULT_DB_ALIAS, keep_parents=False)

