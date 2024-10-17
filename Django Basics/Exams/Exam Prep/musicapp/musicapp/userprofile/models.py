from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from musicapp.userprofile.validators import UserNameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            UserNameValidator(),
         ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        )
    )

