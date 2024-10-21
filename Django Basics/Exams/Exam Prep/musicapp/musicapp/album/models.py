from django.db.models import CASCADE

from django.core.validators import MinValueValidator
from django.db import models

from musicapp.album.choises import GenreChoices
from musicapp.userprofile.models import Profile


class Album(models.Model):
    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        )
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=CASCADE,
        related_name='albums'
    )
