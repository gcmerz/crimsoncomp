
from datetime import date


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.year = year
        self.month = month
        self.day = day

        #year = datetime.date.self.strftime("%Y")
        #month = datetime.date.self.strftime("%B")
        #day = datetime.date.self.strftime("%d")

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError

# TODO: Define an Article class that extends the Content class
class Article(Content):
    def __init__(self, year, month, day, contributors, headline, content, show):
        super(Article, self).__init__(year, month, day, contributors)
        self.headline = headline
        self.content = content

    def show(self):
        print "headline: " + headline + "\ncontributors: "
        a = 0
        while a != (len(contributors) - 1):
            print contributors[a] + " , "
        print contributor[len(contributor)-1] + "\ndate: "
        if month > 9:
            print month + "/"
        else:
            print "0" + month + "/"
        if day > 9:
            print day
        else:
            print "0" + day
        print "/" + "year\n\n" + content

# TODO: Define a Picture class that extends the Content class
class Picture(Content):
    def __init__(self, year, month, day, contributors, title, caption, path, show):
        super(Picture, self).__init__(year, month, day, contributors)
        self.caption = caption
        self.path = path

    def show(self):
        print "headline: " + headline + "\ncontributors: "
        a = 0
        while a != (len(contributors)-1):
            print contributors[a] + " , "
        print contributor[leng(contributor)-1] + "\ndate: "
        if month > 9:
            print month + "/"
        else:
            print "0" + month + "/"
        if day > 9:
                print day
        else:
            print "0" + day
        print "/" + "year\n\n"
        from PIL import Image
        Image.open(path).show
        print caption
