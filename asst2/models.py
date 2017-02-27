
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
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError

# TODO: Define an Article class that extends the Content class
class Article(Content):
    def __init__(self, content, headline, contributors, year, month, day) : 
        Content.__init__(self, year, month, day, contributors)
        self.headline = headline
        self.content = content

    def show(self): 
        print ("Headline: " + self.headline + "\n" + "Contributors: " + self.contributors +
            "\n" + "Date: " + self.creation_date.month + "/" + self.creation_date.day + "/" + 
            self.creation_date.year + "\n" + "Content: " + self.content)

class Picture(Content):
    def __init__(title, caption, path, self, contributors, year, month, day) : 
        Content.__init__(self, year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self): 
        img = Image.open(path)
        print ("Title: " + self.title + "Contributors: " + self.contributors +
            "\n" + "Caption: " + self.caption + "\n" + "Path: " + self.path + 
            "\n" + "Date: " + self.creation_date.month + "/" + 
            self.creation_date.day + "/" + self.creation_date.year)
        img.show()

