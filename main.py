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
        return self.userMovies.get(user.getId(), [])
    
    def getMovieRatings(self, movie):
        return self.movieRatings.get(movie.getId(), {})
    

class MovieRecommendation:
    def __init__(self, ratings):
        self.movieRatings = ratings
    
    def recommendMovie(self, user):
        if len(self.movieRatings.getUserMovies(user)) == 0:
            return self.recommendMovieNewUser()
        else:
            return self.recommendMovieExistingUser(user)
        
    def recommendMovieNewUser(self):
        best_movie = None
        best_rating = 0
        for movie in self.movieRatings.getMovies():
            rating = self.movieRatings.getAverageRatings(movie)
            if rating > best_rating:
                best_movie = movie
                best_rating = rating
        return best_movie.getTitle() if best_movie else None

    def recommendMovieExistingUser(self, user):
        best_movie = None
        similarity_score = float('inf')

        for reviewer in self.movieRatings.getUsers():
            if reviewer.getId() == user.getId():
                continue
            score = self.getSimilarityScore(user, reviewer)
            if score < similarity_score:
                similarity_score = score
                recommended_movie = self.recommendUnwatchedMovie(user, reviewer)
                best_movie = recommended_movie if recommended_movie else best_movie
        return best_movie.getTitle() if best_movie else None
    
    def getSimilarityScore(self, user1, user2):
        user1_id = user1.getId()
        user2_id = user2.getId()
        user2_movies = self.movieRatings.getUserMovies(user2)
        score = float('inf')

        for movie in user2_movies:
            cur_movie_ratings = self.movieRatings.getMovieRatings(movie)
            if user1_id in cur_movie_ratings:
                score = 0 if score == float('inf') else score
                score += abs(cur_movie_ratings[user1_id].value - cur_movie_ratings[user2.id].value)
        return score
    
    def recommendUnwatchedMovie(self, user, reviewer):
        user_id = user.getId()
        reviewer_id = reviewer.getId()
        best_movie = None
        best_rating = 0

        reviewer_movies = self.movieRatings.getUserMovies(reviewer)
        for movie in reviewer_movies:
            cur_movie_ratings = self.movieRatings.getMovieRatings(movie)
            if user_id not in cur_movie_ratings and cur_movie_ratings[reviewer_id].value > best_rating:
                best_movie = movie
                best_rating = cur_movie_ratings[reviewer_id].value
        return best_movie

user1 = User(1, 'User 1')
user2 = User(2, 'User 2')
user3 = User(3, 'User 3')

movie1 = Movie(1, 'Batman Begins')
movie2 = Movie(2, 'Liar Liar')
movie3 = Movie(3, 'The Godfather')

ratings = RatingRegister()
ratings.addRating(user1, movie1, MovieRating.FIVE)
ratings.addRating(user1, movie2, MovieRating.TWO)
ratings.addRating(user2, movie2, MovieRating.TWO)
ratings.addRating(user2, movie3, MovieRating.FOUR)

recommender = MovieRecommendation(ratings)

print(recommender.recommendMovie(user1)) # The Godfather
print(recommender.recommendMovie(user2)) # Batman Begins
print(recommender.recommendMovie(user3)) # Batman Begins