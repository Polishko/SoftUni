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

    approved = models.BooleanField(
        default=False,
    )

    language = models.CharField(
        max_length=LANGUAGE_MAX_LENGTH,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )

    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True,
    )

    class Meta:
        permissions = [
            ('can_approve_posts', 'Can approve posts'),
        ]

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
