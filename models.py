from datetime import date
import Image


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError

class Article(Content):

    def __init__(self, year, month, day, contributors, headline, content):

        super(Article, self).__init__(year, month, day, contributors)
        self.content = content
        self.headline = headline
    
    def show(self):
       
        s = '{0} was written by {1}\n{2}, {3}, {4}\n{5}\n{6}'.format(self.headline, self.contributors, self.creation_date.year, self.creation_date.month, self.creation_date.day, self.headline, self.content)
        print s

class Picture(Content):
    def __init__(self, year, month, day, contributors, title, caption, path):

        super(Picture, self).__init__(year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self):

        r = '{0} was written by {1}\nLink: {2}\n{3}, {4}, {5}\n{6}'.format(self.title, self.contributors, self.path, self.creation_date.year, self.creation_date.month, self.creation_date.day, self.caption)
        im = Image.open("puppy.jpg")
        im.show()
        print r
# TODO: Define an Article class that extends the Content class


# TODO: Define a Picture class that extends the Content class
