from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE


class Fruit(models.Model):
    fruit_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
        validators=(
            MinLengthValidator(2),
        ),
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.',
        }
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        to='userprofile.Profile',
        on_delete=CASCADE,
        null=False,
        blank=True,  # maybe not needed
    )
