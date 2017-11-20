from datetime import date
from PIL import Image


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # date object for the year-month-day that the content was created
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


class Article(Content):

    def __init__(self, year, month, day, contributors, headline, content):
        # give the article object all the attributes of generic content objects
        super(Article, self).__init__(year, month, day, contributors)

        # string for the headline of the article
        self.headline = headline

        # string holding the text of the content
        self.content = content

    # override the Content class's show() method to display the article
    def show(self):
        print self.headline + "\n\n" + self.content


class Picture(Content):

    def __init__(self, year, month, day, contributors, title, caption, path):
        # give the picture object the Content class's attributes
        super(Picture, self).__init__(year, month, day, contributors)

        # the title of the image
        self.title = title

        # the caption for the image
        self.caption = caption

        # file path to where the image is locally stored
        self.path = path

    # override the Content class's show() method to display the image
    def show(self):
        Image.open(self.path).show()
