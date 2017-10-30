from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()
    def show(self):
        print(self.title)
        print(self.subtitle)
        for c in self.contributors.all(): 
            c.show()
        print(self.pub_date)
        print(self.text)
        return None

class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
    middle_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    def show(self):
        print(self.first_name)
        print(self.middle_name)
        print(self.last_name)
    def die(self):
        self.delete()
        return None