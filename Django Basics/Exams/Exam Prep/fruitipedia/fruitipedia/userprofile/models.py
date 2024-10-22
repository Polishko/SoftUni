from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.userprofile.validators import UserNameValidator


class Profile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=(
            MinLengthValidator(2),
            UserNameValidator(),
        )
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=(
            MinLengthValidator(1),
            UserNameValidator(),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
        unique=True,
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            MinLengthValidator(8),
        ),
        help_text='*Password length requirements: 8 to 20 characters',
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        default=18,
    )
