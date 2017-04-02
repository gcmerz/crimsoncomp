
from datetime import date
from PIL import Image 
import glob, os

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
       
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # date of creation 
        # help from https://docs.python.org/2/library/datetime.html
        self.year = datetime.year(year)
        self.month = datetime.month(month)
        self.day = datetime.day(day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError

class Article(Content):
    def __init__(self, headline, content, year, month, day):
        
        # help with super from https://docs.python.org/2/library/functions.html#super
        super(Article, self).__init__(year, month, day, contributors)
        self.headline = headline
        self.content = content 

    def show(self):
        print 'Headline: %s \n Content: %s \n Creation: %s \n Contributors: %s' (self.headline, self.content, self.year, self.month, self.day, self.contributors)
        # code from http://pillow.readthedocs.io/en/latest/reference/Image.html
        im = Image.open("puppy.jpg")
        return im 

class Picture(Content):

    def __init__(self, title, caption, path, year, month, day, contributors):
        
        self.title = title
        self.caption = caption 
        self.path = path 

    def show(self):
        print 'Title %s \n Caption: %s \n Path: ' (self.title, self.caption, self.path, self.year, self.month, self.day, self.contributors)

