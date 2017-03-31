from PIL import Image
from datetime import date


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


class Article(Content):
    
    def __init__(self, year, month, day, contributors, headline, content):
        super(Article, self).__init__(year, month, day, contributors)

        self.headline = headline
        self.content = content

    def show(self):
        string = '\n-----' + self.headline + '-----\n\n'
        string += 'Author(s): ' + ', '.join(self.contributors) + '\n'
        string += 'Date created: ' + self.creation_date.isoformat() + '\n\n'
        string += str(self.content) + '\n'
        print string


class Picture(Content):
    
    def __init__(self, year, month, day, contributors, title, caption, path):
        super(Picture, self).__init__(year, month, day, contributors)

        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        string = '\n-----' + self.title + '-----\n\n'
        string += 'Author(s): ' + ', '.join(self.contributors) + '\n'
        string += 'Date created: ' + self.creation_date.isoformat() + '\n\n'
        string += self.caption + '\n'
        print string
        Image.open(self.path).show()
