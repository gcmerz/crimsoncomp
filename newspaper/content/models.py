
from django.db import models
from django.utils import timezone

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')

    #from djangogirls 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #from django girls
    def __str__(self):
        return self.title
    #

class Article(Content):
    text = models.TextField()

    def die(self):
    	models.Model.delete 



class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
