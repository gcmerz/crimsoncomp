
from datetime import date
today = date.today()


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, contributors, year=today.year, month=today.month, day=today.day):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Define an Article class that extends the Content class
class Article(Content):
    def __init__(self, contributors, headline, content, year=today.year, month=today.month, day=today.day):
        Content.__init__(self, contributors, year, month, day)
        self.headline = headline
        self.content = content

    def show():
        dt ={"contributors": self.contributors,
             "headline": self.headline,
             "content": self.content,
             "year": self.creation_date.year,
             "month": self.creation_date.month,
             "day": self.creation_date.day}
        print dt

# TODO: Define a Picture class that extends the Content class


class Picture(Content):
    def __init__(self, contributors, title, caption, path, year=today.year, month=today.month, day=today.day):
        Content.__init__(self, contributors, year, month, day)
        self.title = title
        self.caption = caption
        self.path = path
    def show():
        dt ={"contributors": self.contributors,
             "title": self.title,
             "caption": self.caption,
             "path": self.path,
             "year": self.creation_date.year,
             "month": self.creation_date.month,
             "day": self.creation_date.day}
        print dt

