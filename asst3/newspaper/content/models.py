from __future__ import unicode_literals

from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor', related_name='content')
    pub_date = models.DateTimeField('date published')

class Article(Content):
    text = models.TextField()

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    define die(self):
        (self.delete)
class Image(Content):
    kicker = models.CharField(max_length=500)
    caption = models.CharField(max_length = 1000)
    contributors = models.ManyToManyField('Contributor', related_name='content')

# Create your models here.
