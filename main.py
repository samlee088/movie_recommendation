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
    
from enum import Enum

class MovieRating(Enum):
    NOT_RATED = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

