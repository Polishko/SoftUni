from django.db import models

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
