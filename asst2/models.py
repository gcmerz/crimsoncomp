from datetime import date
t = date.today()

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []


    # defaults to current date, can be overridden
    def __init__(self, contributors, year=t.year, month=t.month, day=t.day):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # set the creation date
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# Define an Article class that extends the Content class
class Article(Content):
    # is this bad formatting?
    # I felt like it was the only reasonable way to do this
    def __init__(self,
                 contributors,
                 headline,
                 content,
                 year=t.year,
                 month=t.month,
                 day=t.day):
        # initialize as a content object
        Content.__init__(self, contributors, year, month, day)

        # an attribute for a headline
        self.headline = headline

        # an attribute for the content
        self.content = content

    def show(self):
        # make a dictionary to be printed that has the new attributes
        to_show = {"headline": self.headline,
                   "contributors": self.contributors,
                   "content": self.content,
                   "year": self.creation_date.year,
                   "month": self.creation_date.month,
                   "day": self.creation_date.day}

        # print to console
        print(to_show)

# Define a Picture class that extends the Content class
class Picture(Content):
    t = date.today()
    def __init__(self,
                 title,
                 caption,
                 path,
                 contributors,
                 year=t.year,
                 month=t.month,
                 day=t.day):
        # initialize as a content object
        Content.__init__(self, contributors, year, month, day)

        # an attribute for a headline
        self.title = title

        # an attribute for the content
        self.caption = caption

        # an attribute for the path to the file
        self.path = path

    def show(self):
        # make a dictionary to be printed that has the new attributes
        to_show = {"title": self.title,
                   "caption": self.caption,
                   "path": self.path,
                   "year": self.creation_date.year,
                   "month": self.creation_date.month,
                   "day": self.creation_date.day}

        # print to console
        print(to_show)
