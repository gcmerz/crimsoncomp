
from datetime import date

import pprint
  
  class Content(object):
      # list to keep track of all pieces of content
 @@ -12,17 +12,35 @@ def __init__(self, year, month, day, contributors):
  
         # TODO: Delete the following line and replace it with a line
         # that stores the year, month, and day (hint: check out datetime.date)
         self.creation_date = None
         self.creation_date = date(year, month, day)
  
         # list of contirbutors
         self.contributors = contributors
  
     # this defines a show method that has nothing in it, to be overridden later
     def show(self):
         raise NotImplementedError
 
         print self.creation_date
         print self.contributors
  
 # TODO: Define an Article class that extends the Content class
  
 class Article(Content):
     def __init__(self, year, month, day, contributors, headline, content):
         super(Article, self).__init__(year, month, day, contributors)
         self.headline = headline
         self.content = content
 
     def show(self):
         return PrettyPrinter.pformat(object)
  
 # TODO: Define a Picture class that extends the Content class
 
 class Picture(Content):
     def __init__(self, year, month, day, contributors, title, caption, path):
         super(Picture, self).__init__(year, month, day, contributors)
         self.title = title
         self.caption = caption
         self.path = path
 
     def show(self):
         return PIL.Image.open(fp, mode = 'r') 
