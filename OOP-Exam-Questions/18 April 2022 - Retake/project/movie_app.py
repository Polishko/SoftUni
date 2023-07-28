from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list = []
        self.users_collection: list = []

    def __find_user(self, username: str):
        for user in self.users_collection:
            if user.username == username:
                return user

    def register_user(self, username: str, age: int):
        if self.__find_user(username):
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if not user:
            raise Exception("This user does not exist!")

        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.__find_user(username)
        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        for attr_name, value in kwargs.items():
            if attr_name == "title":
                movie.title = value
            elif attr_name == "year":
                movie.year = value
            elif attr_name == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.__find_user(username)
        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)

        if user.username == movie.owner.username:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        return "\n".join(movie.details() for movie in sorted_movies)

    def __str__(self):
        result = []

        if self.users_collection:
            result.append(f"All users: {', '.join(user.username for user in self.users_collection)}")
        else:
            result.append("All users: No users.")

        if self.movies_collection:
            result.append(f"All movies: {', '.join(movie.title for movie in self.movies_collection)}")
        else:
            result.append("All movies: No movies.")

        return "\n".join(result)
