import os
from decimal import Decimal

import django
from django.db.models import Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from main_app.models import Director, Movie, Actor
from datetime import date


# director_1 = Director.objects.create(
#     full_name="Director 1",
#     birth_date=date(1980, 1, 1),
#     nationality="Country 1",
#     years_of_experience=10
# )
#
# director_2 = Director.objects.create(
#     full_name="Director 2",
#     birth_date=date(1975, 5, 5),
#     nationality="Country 2",
#     years_of_experience=15
# )
#
# # Create Actors
# actor_1 = Actor.objects.create(
#     full_name="Actor 1",
#     birth_date=date(1990, 3, 15),
#     nationality="Country 3",
#     is_awarded=True
# )
#
# actor_2 = Actor.objects.create(
#     full_name="Actor 2",
#     birth_date=date(1985, 7, 20),
#     nationality="Country 4",
#     is_awarded=False
# )
#
# actor_3 = Actor.objects.create(
#     full_name="Actor 3",
#     birth_date=date(1982, 10, 8),
#     nationality="Country 5",
#     is_awarded=True
# )
#
# actor_4 = Actor.objects.create(
#     full_name="Actor 4",
#     birth_date=date(1995, 2, 25),
#     nationality="Country 6",
#     is_awarded=False
# )
#
# # Create Movies
# movie_1 = Movie.objects.create(
#     title="Movie 1",
#     release_date=date(2020, 5, 1),
#     storyline="Storyline for Movie 1",
#     genre="Action",
#     rating=8.5,
#     is_classic=True,
#     is_awarded=True,
#     director=director_1,
#     starring_actor=actor_1
# )
# movie_1.actors.set([actor_2, actor_3])
#
# movie_2 = Movie.objects.create(
#     title="Movie 2",
#     release_date=date(2018, 8, 15),
#     storyline="Storyline for Movie 2",
#     genre="Comedy",
#     rating=7.2,
#     is_classic=False,
#     is_awarded=False,
#     director=director_1,
#     starring_actor=actor_2
# )
# movie_2.actors.set([actor_1, actor_3])
#

# director_3 = Director.objects.create(
#     full_name="Director 3",
#     birth_date=date(1982, 3, 10),
#     nationality="Country 3",
#     years_of_experience=8
# )
#
# director_4 = Director.objects.create(
#     full_name="Director 4",
#     birth_date=date(1978, 9, 22),
#     nationality="Country 4",
#     years_of_experience=12
# )
#
# # Create More Actors
# actor_5 = Actor.objects.create(
#     full_name="Actor 5",
#     birth_date=date(1993, 6, 5),
#     nationality="Country 7",
#     is_awarded=True
# )
#
# actor_6 = Actor.objects.create(
#     full_name="Actor 6",
#     birth_date=date(1987, 11, 30),
#     nationality="Country 8",
#     is_awarded=False
# )
#
# actor_7 = Actor.objects.create(
#     full_name="Actor 7",
#     birth_date=date(1980, 4, 18),
#     nationality="Country 9",
#     is_awarded=True
# )
#
# # Create More Movies
# movie_3 = Movie.objects.create(
#     title="Movie 3",
#     release_date=date(2022, 2, 28),
#     storyline="Storyline for Movie 3",
#     genre="Drama",
#     rating=9.0,
#     is_classic=True,
#     is_awarded=True,
#     director=director_3,
#     starring_actor=actor_5
# )
# movie_3.actors.set([actor_5, actor_6])
#
# movie_4 = Movie.objects.create(
#     title="Movie 4",
#     release_date=date(2019, 11, 12),
#     storyline="Storyline for Movie 4",
#     genre="Action",
#     rating=7.8,
#     is_classic=False,
#     is_awarded=False,
#     director=director_3,
#     starring_actor=actor_7
# )
# movie_4.actors.set([actor_5, actor_6])

# test DirectorManager
# directors_by_movie_Count = Director.objects.get_directors_by_movies_count()
# for director in directors_by_movie_Count:
#     print(f"{director.full_name} has {director.movie_count} movies")

def get_directors(search_name=None, search_nationality=None):
    # alternative 1
    if not search_name and not search_nationality:
        return ""

    result = []
    if search_name and search_nationality:
        searched_directors = Director.objects.filter(full_name__icontains=search_name,
                                                     nationality__icontains=search_nationality).all()
    elif not search_name:
        searched_directors = Director.objects.filter(nationality__icontains=search_nationality).all()
    else:
        searched_directors = Director.objects.filter(full_name__icontains=search_name).all()

    if not searched_directors:
        return ""

    ordered_directors = searched_directors.order_by("full_name")

    for director in ordered_directors:
        result.append(f"Director: {director.full_name}, "
                      f"nationality: {director.nationality}, "
                      f"experience: {director.years_of_experience}")

    return "\n".join(result)

    #alternative 2
    if not search_name and not search_nationality:
        return ""

    result = []
    query = Q()
    search_name_query = Q(nationality__icontains=search_nationality)
    search_nationality_query = Q(full_name__icontains=search_name)

    if search_name and search_nationality:
        query |= search_name_query & search_nationality_query
    elif not search_name:
        query |= search_nationality_query
    else:
        query |= search_name_query

    directors = Director.objects.filter(query).order_by("full_name")

    if not directors:
        return ""

    for director in directors:
        result.append(f"Director: {director.full_name}, "
                      f"nationality: {director.nationality}, "
                      f"experience: {director.years_of_experience}")

    return "\n".join(result)

    # alternative 3
    # collect query conditions in a dictionary then pass as **kwargs to filter


# test get_directors function

# print(get_directors())
# print(get_directors("rect", "Ount"))
# print(get_directors(search_nationality="Ount"))
# print(get_directors(search_nationality="p"))
# print(get_directors(search_name="p"))
# print(get_directors(search_name="DIR"))

#
# directors = Director.objects.select_related("director_movies").all()
# for director in directors:
#     print(director.full_name, director.director_movies)


def get_top_director():
    director_with_most_movies = Director.objects.get_directors_by_movies_count().first()

    if director_with_most_movies:
        return (f"Top Director: {director_with_most_movies.full_name},"
                f" movies: {director_with_most_movies.movie_count}.")
    return ""

    # if director_with_most_movies:
    #     return (f"Top Director: {director_with_most_movies.full_name},"
    #             f" movies: {len(director_with_most_movies.director_movies.all())}.")
    # return ""

# test
# print(get_top_director())


def get_top_actor():
    actor_with_most_movies = (Actor.objects.prefetch_related("starring_movies").
                              annotate(
        movie_count=Count("starring_movies"),
        ave_rating=Avg("starring_movies__rating")).
                              order_by("-movie_count", "full_name")).first()

    if not actor_with_most_movies or not actor_with_most_movies.movie_count:
        return ""

    actor_movies_list = ", ".join(movie.title for movie in actor_with_most_movies.starring_movies.all())

    return (f"Top Actor: {actor_with_most_movies.full_name}, "
            f"starring in movies: {actor_movies_list}, "
            f"movies average rating: {actor_with_most_movies.ave_rating:.1f}")


# print(get_top_actor())


def get_actors_by_movies_count():
    all_actors = (Actor.objects.prefetch_related("actor_movies").
                  annotate(num_movies=Count("actor_movies")).
                  order_by("-num_movies", "full_name"))[:3] # will retrieve even when less than 3

    if not all_actors or not Movie.objects.all():
        return ""

    result = []

    # all_actors = (Actor.objects.prefetch_related("actor_movies").
    #               annotate(num_movies=Count("actor_movies")).
    #               order_by("-num_movies", "full_name")).all()
    #
    # if not all_actors or not Movie.objects.all():
    #     return ""
    #
    # result = []
    # actors = all_actors[:3] if len(all_actors) >= 3 else all_actors

    for actor in all_actors:
        result.append(f"{actor.full_name}, participated in {actor.num_movies} movies")

    return "\n".join(result)


# print(get_actors_by_movies_count())


def get_top_rated_awarded_movie():
    movie = (Movie.objects.
             select_related("starring_actor").
             prefetch_related("actors").
             filter(is_awarded=True).
             order_by("-rating", "title").first())

    if not movie:
        return ""

    actors_list = ", ".join(actor.full_name for actor in movie.actors.all().order_by("full_name"))
    starring_actor_name = "N/A" if not movie.starring_actor else movie.starring_actor.full_name

    return (f"Top rated awarded movie: {movie.title},"
            f" rating: {movie.rating:.1f}."
            f" Starring actor: {starring_actor_name}. Cast: {actors_list}.")


# print(get_top_rated_awarded_movie())


def increase_rating():
    #alternative 1
    movies = Movie.objects.filter(is_classic=True, rating__lt=10.0).all()

    if not movies:
        return "No ratings increased."

    for movie in movies:
        new_rating = min(movie.rating + Decimal(0.1), Decimal(10.0))
        movie.rating = new_rating
        movie.save()

    return f"Rating increased for {len(movies)} movies."


# print(increase_rating())
