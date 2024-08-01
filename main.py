class Movie:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getId(self):
        return self.id