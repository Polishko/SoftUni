from django.db import models
from django.db.models import CASCADE

from forumApp.posts.choices import LanguageChoices
from forumApp.posts.validators import BadLanguageValidator


class Post(models.Model):
    TITLE_MAX_LENGTH = 100
    AUTHOR_MAX_LENGTH = 30
    LANGUAGE_MAX_LENGTH = 20

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    content = models.TextField(
        validators=(
            BadLanguageValidator(),
        )
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    language = models.CharField(
        max_length=LANGUAGE_MAX_LENGTH,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
