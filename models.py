+
 +from datetime import date
 +from PIL import Image
 +
 +
 +class Content(object):
 +    # list to keep track of all pieces of content
 +    existing_content = []
 +
 +    def __init__(self, year, month, day, contributors):
 +        # log each piece of content as existing upon creation
 +        self.existing_content.append(self)
 +
 +        # TODO: Delete the following line and replace it with a line
 +        # that stores the year, month, and day (hint: check out datetime.date)
 +        self.creation_date = date(year, month, day)
 +
 +        # list of contirbutors
 +        self.contributors = contributors
 +
 +    # this defines a show method that has nothing in it, to be overridden later
 +    def show(self):
 +        raise NotImplementedError
 +
 +
 +# TODO: Define an Article class that extends the Content class
 +class Article(Content):
 +    # define the class with all the inputs that Content had plus the new ones
 +    def __init__(self, year, month, day, contributors, headline, content):
 +        # calls Content's initializer
 +        Content.__init__(self, year, month, day, contributors)
 +
 +        # stores headline value
 +        self.headline = headline
 +        # stores content string
 +        self.content = content
 +
 +    def show(self):
 +        print("Date Created: " + creation_date + "\nContributors: " + contributors + "\nHeadline: " + headline + "\nContent: " + content)
 +
 +# TODO: Define a Picture class that extends the Content class
 +class Picture(Content):
 +    # define the class with all the inputs that Content had plus the new ones
 +    def __init__(self, year, month, day, contributors, title, caption, path):
 +        # calls Content's initializer
 +        Content.__init__(self, year, month, day, contributors)
 +
 +        # stores title string
 +        self.title = title
 +        # stores caption string
 +        self.caption = caption
 +        # stores path string
 +        self.path = path
 +
 +    def show(self):
 +        print("Date Created: " + creation_date + "\nContributors: " + contributors + "\nTitle: " + title + "\nCaption: " + caption)
 +        im = Image.open(path)
 +        im.show() 