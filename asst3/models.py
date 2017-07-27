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
    text = models.TextField()

    def show(self):
        print self.title
        print self.subtitle
        print self.pub_date
        print self.contributors, '\n'
        print self.text


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def die(self):
        self.delete()
