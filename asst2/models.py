import datetime
from PIL import Image


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = datetime.date(year,month,day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Defined an Article
class Article(Content):
    def __init__(self, year, month, day, contributors, headline, content):
        Content.__init__(self, year, month, day, contributors)
        self.headline = headline
        self.content = content
    def show(self):
        print(self.headline+"\n"+self.content)

# TODO: Defined a Picture Class
class Picture(Content):
    def __init__(self,year,month,day,contributors,title,caption,path):
        Content.__init__(self,year,month,day,contributors)
        self.title = title
        self.caption = caption
        self.path = path
    def show(self):
        print(self.title+"\n"+self.caption)
        pic = Image.open(self.path,mode='r')
	pic.show()
