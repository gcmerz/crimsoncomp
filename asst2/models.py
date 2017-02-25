
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
    headline = "headline"
    content = "content"
    def __init__(self, year, month, day, headline, content, contributors):
        Content.__init__(self, year, month, day, contributors)
        self.headline = headline
        self.content = content

    def show(self):
        # prints out information about article 
        print ("Date: " + self.creation_date.strftime('%m/%d/%Y') + "\n" +
        "Contributors: " + str(self.contributors) + "\n" +
        "Headline: " + self.headline + "\n" +
        "Content: " + self.content + "\n")

# TODO: Define a Picture class that extends the Content class
class Picture(Content):
    title = "title"
    caption = "caption"
    def __init__(self, year, month, day, title, caption, path, contributors):
        Content.__init__(self, year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        # opens image using Image module
        Image.open(self.path).show()
        # prints out information about image
        print ("Date: " + self.creation_date.strftime('%m/%d/%Y') + "\n" +
        "Contributors: " + str(self.contributors) + "\n" +
        "Title: " + self.title + "\n" +
        "Caption: " + self.caption + "\n" +
        "Path: " + str(self.path) + "\n")
