from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CharField, URLField

from myplantapp.userprofile.validators import UserNameValidator


class Profile(models.Model):
    username = CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(
            MinLengthValidator(2),
        ),
        verbose_name='Username',
    )

    first_name = CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            UserNameValidator(),
        ),
        verbose_name='First Name',
    )

    last_name = CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            UserNameValidator(),
        ),
        verbose_name='First Name',
    )

    profile_picture = URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    def get_full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
