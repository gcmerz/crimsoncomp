
from datetime import date
from PIL import Image

t = date.today()


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, month = t.month, day = t.day, year = t.year, contributors = None):
        # log eachpiece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)


        # list of contirbutors
        self.contributors = contributors

    # show method
    def show(self):
        print "Published on: " + str(self.creation_date.month) +  ", " + str(self.creation_date.day) + ", " + str(self.creation_date.year)


# TODO: Define an Article class that extends the Content class
class Article(Content):

    def __init__(self, headline, content, **kwargs):
        super(Article, self).__init__(**kwargs)

        # article healine and conten
        self.headline = headline
        self.content = content

    def show(self):
        super(Article, self).show()
        print self.headline
        print self.content


# TODO: Define a Picture class that extends the Content class
class Picture(Content):

    def __init__(self, title, caption, path, **kwargs):
        super(Picture, self).__init__(**kwargs)

        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        super(Picture, self).show()
        im = Image.open(self.path)
        print self.title
        im.show()
        print self.caption



