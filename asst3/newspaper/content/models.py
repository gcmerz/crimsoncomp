from django.db import models
from django.utils import timezone


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content, models.Model):
    title = Content.title
    subtitle = Content.subtitle
    contributors = Content.contributors
    pub_date = Content.pub_date

    text = models.TextField('article text', default='TEXT')

    def show(self):
        string = "Title: " + self.title + "\nSubtitle: " + self.subtitle \
        + "\nPublished: " + self.pub_date + "\n\n" + self.text
        return string

    def __str__(self):
        return self.title


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def die(self):
        self.models.delete()

    def __str__(self):
        return self.first_name + " " + self.last_name
