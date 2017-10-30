from datetime import date

class Content(object):
    existing_content = []
    def __init__(self, year, month, day, contributors):
        self.existing_content.append(self)
        self.creation_date = date(year, month, day);
        self.contributors = contributors
    def show(self):
        raise NotImplementedError

class Picture(Content):  
    def __init__(self, year, month, day, contributors, title, caption, path):
        super(Picture, self).__init__(year, month, day, contributors) #calls Content to store these attributes
        self.title = title #includes Picture-specific attributes
        self.caption = caption
        self.path = path
    def show(self):
        print self.title+"\n"+"".join(self.contributors)+"\n"+str(self.creation_date)+"\n"+self.caption+"\n"+self.path

class Article(Content):
    def __init__(self, year, month, day, contributors, headline, content):
        super(Article, self).__init__(year, month, day, contributors) #calls Content to store these attributes
        self.headline = headline #includes Article-specific attributes
        self.content = content
    def show(self):
        print self.headline+"\n"+"".join(self.contributors)+"\n"+str(self.creation_date)+"\n"+self.content