from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from main_app.mixins import ContentMixin, PublishedMixin
from main_app.managers import AuthorManager


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3)
        ]
    )
    email = models.EmailField(
        unique=True
    )
    is_banned = models.BooleanField(
        default=False
    )
    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005)
        ]
    )
    website = models.URLField(
        null=True,
        blank=True
    )

    objects = AuthorManager()


class Article(ContentMixin, PublishedMixin):
    CATEGORIES = [
        ("Technology", "Technology"),
        ("Science", "Science"),
        ("Education", "Education")
    ]

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5)
        ]
    )
    category = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default="Technology"
    )
    authors = models.ManyToManyField(
        to=Author,
        related_name="articles"
    )


class Review(ContentMixin, PublishedMixin):
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ]
    )
    author = models.ForeignKey(
        to=Author,
        related_name="author_reviews",
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        to=Article,
        related_name="article_reviews",
        on_delete=models.CASCADE
    )

