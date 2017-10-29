
from datetime import date
from PIL import Image

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # stores the year, month, and day
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Define an Article class that extends the Content class
class Article(Content):
    def __init__(self, year, month, day, headline, content, contributors):
        super(self.__class__, self).__init__(year, month, day, contributors)
        self.headline = headline
        self.content = content

    def show(self):
        print 'Date: %s' % self.creation_date
        print 'Contributors:'
        print ', '.join(self.contributors)
        print 'Headline: %s' % self.headline
        print 'Content: %s' % self.content


# TODO: Define a Picture class that extends the Content class
class Picture(Content):
    def __init__(self, year, month, day, title, caption, path, contributors):
        super(self.__class__, self).__init__(year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        print 'Date: %s' % self.creation_date
        print 'Contributors:'
        print ', '.join(self.contributors)
        print 'Title: %s' % self.title
        print 'Caption: %s' % self.caption
        im = Image.open(self.path)

