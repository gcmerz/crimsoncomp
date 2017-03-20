
from datetime import date
from PIL import Image

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.day = datetime.date.today().day        

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        print self.all


# TODO: Define an Article class that extends the Content class

class Article(Content):

    def __init__(headline, content):
        self.headline = headline

        self.content = content

    def show(self):
        print self.headline
        print self.content

# TODO: Define a Picture class that extends the Content class

class Picture(Content):

    def __init__(title, caption, path):
        self.title = title

        self.caption = caption

        self.path = path

    def show(self):
        im = Image.open(self.path)
        im.show()
        print self.title
        print self.caption
