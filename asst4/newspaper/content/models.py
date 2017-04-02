from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from datetime import datetime

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published', default=datetime.now)

class Article(Content):
    text = HTMLField()

class Image(Content):
    filepath = models.FilePathField()

class Contributor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateTimeField('birthday', null=True)

    def die(self):
        self.delete()
