import os
import random

import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review
from populate_db import populate_model_with_data
# Create and run your queries within functions

# populate_model_with_data(Author)
# populate_model_with_data(Article)


# def create_reviews():
#     for _ in range(10):
#         # Choose a random author and article
#         author = Author.objects.get(pk=random.randint(1, 10))
#         article = Article.objects.get(pk=random.randint(1, 10))
#
#         # Generate random rating between 1.0 and 5.0
#         rating = round(random.uniform(1.0, 5.0), 1)
#
#         # Create the review
#         review = Review.objects.create(
#             content="content.",
#             rating=rating,
#             author=author,
#             article=article
#         )
#
#
# # Call the function to create reviews
# create_reviews()

#test Authormanager
# print(Author.objects.get_authors_by_article_count())


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    query = Q()

    if search_name and search_email:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)
    elif search_name is None:
        query = Q(email__icontains=search_email)
    else:
        query = Q(full_name__icontains=search_name)

    return "\n".join(f"Author: {a.full_name},"
                     f" email: {a.email},"
                     f" status: {'Banned' if a.is_banned == True else 'Not Banned'}"
                     for a in Author.objects.filter(query).order_by("-full_name"))


# print(get_authors("THor"))
# print(get_authors())
# print(get_authors("LAla"))


def get_top_publisher():
    author = Author.objects.get_authors_by_article_count().first()

    if author is None or not author.num_articles:
        return ""

    return f"Top Author: {author.full_name} with {author.num_articles} published articles."


# print(get_top_publisher())


def get_top_reviewer():
    author = (Author.objects.
              prefetch_related("author_reviews").
              annotate(num_reviews=Count("author_reviews")).
              order_by("-num_reviews", "email").
              first())

    if author is None or not author.num_reviews:
        return ""

    return f"Top Reviewer: {author.full_name} with {author.num_reviews} published reviews."


# print(get_top_reviewer())


def get_latest_article():
    article = (Article.
               objects.prefetch_related("article_reviews").
               annotate(ave_rating=Avg("article_reviews__rating")).
               order_by("-published_on").first())

    if article is None:
        return ""

    ave_rating = article.article_reviews.aggregate(Avg("rating"))["rating__avg"]
    ave_rating = ave_rating if ave_rating is not None else 0

    authors = ", ".join(a.full_name for a in article.authors.all().order_by("full_name"))

    return (f"The latest article is: "
            f"{article.title}."
            f" Authors: {authors}."
            f" Reviewed: {article.article_reviews.count()} times."
            f" Average Rating: {ave_rating:.2f}.")


# print(get_latest_article())


def get_top_rated_article():
    article = (Article.objects.
               prefetch_related("article_reviews").
               annotate(ave_rating=Avg("article_reviews__rating")).
               exclude(ave_rating__isnull=True).
               order_by("-ave_rating", "title").
               first()
               )

    if article is None:
        return ""

    return (f"The top-rated article is:"
            f" {article.title},"
            f" with an average rating of {article.ave_rating:.2f},"
            f" reviewed {article.article_reviews.count()} times.")


# print(get_top_rated_article())


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = Author.objects.prefetch_related("author_reviews").filter(email=email).first()

    if author is None:
        return "No authors banned."

    num_reviews = author.author_reviews.count()
    author.is_banned = True
    author.author_reviews.all().delete()
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."


# print(ban_author())



