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

class RatingRegister:
    def __init__(self):
        self.userMovies = {}
        self.movieRatings = {}

        self.movies = []
        self.users = []

    def addRating(self, user, movie, rating):
        if movie.getId() not in self.movieRatings:
            self.movieRatings[movie.getId()] = {}
            self.movies.append(movie)
        if user.getId() not in self.userMovies:
            self.userMovies[user.getId()] = []
            self.users.append(user)
        self.userMovies[user.getId()].append(movie)
        self.movieRatings[movie.getId()][user.getId()] = rating
    
    def getAverageRatings(self, movie):
        if movie.getId() not in self.movieRatings:
            return MovieRating.NOT_RATED.value
        ratings = self.movieRatings[movie.getId()].values()
        ratingValues = [rating.value for rating in ratings]
        return sum(ratingValues) / len(ratings)
    
    def getUsers(self):
        return self.users

    def getMovies(self):
        return self.movies
    
    def getUserMovies(self, user):
        return self.userMovies.get(user.getIdI, [])
    
    def getMovieRatings(self, movie):
        return self.movieRatings.get(movie.getIdId(), {})