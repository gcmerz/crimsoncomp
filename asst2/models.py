<<<<<<< HEAD

from datetime import date
=======
import datetime
from PIL import Image
>>>>>>> 4ba5bcb26dbde37acdb3daa6a05d4a3b719f8e90


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
<<<<<<< HEAD
        self.creation_date = None
=======
        self.creation_date = {year: datetime.date.today().year, month: datetime.date.today().month, day: datetime.date.today().day}
>>>>>>> 4ba5bcb26dbde37acdb3daa6a05d4a3b719f8e90

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Define an Article class that extends the Content class
<<<<<<< HEAD


# TODO: Define a Picture class that extends the Content class
=======
class Article(Content): 
    def __init__(self, headline, content, year, month, day, contributors): 
        super(Article, self).__init__(year, month, day, contributors)

        self.content = content
        self.headline = headline 

    def show(self): 
        print "{0} \n {1}".format(self.headline, self.content)


# TODO: Define a Picture class that extends the Content class
class Picture(Content):
    def __init__(self, title, caption, path, year, month, day, contributors): 
        super(Picture, self).__init__(year, month, day, contributors)

        self.title = title
        self.caption = caption
        self.path = path

    def show(self): 
        im = Image.open(path)
        im.show()
        print "Title: {0}\n Caption: {1}\n Path: {2}".format(self.title, self.caption, self.path)
>>>>>>> 4ba5bcb26dbde37acdb3daa6a05d4a3b719f8e90
