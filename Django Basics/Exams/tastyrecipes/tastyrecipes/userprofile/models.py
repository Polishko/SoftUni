from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CharField, BooleanField, TextField

from tastyrecipes.userprofile.validators import NameValidator


class Profile(models.Model):
    nickname = CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=20,
        validators=(
            MinLengthValidator(2, message='Nickname must be at least 2 chars long!'),
        ),
        verbose_name='Nickname',
    )

    firstname = CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            NameValidator(),
        ),
        verbose_name='First Name',
    )

    lastname = CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            NameValidator(),
        ),
        verbose_name='Last Name',
    )

    chef = BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name='Chef',
    )

    bio = TextField(
        blank=True,
        null=True,
        verbose_name='Bio'
    )

    def get_full_name(self):
        return f'{self.firstname.capitalize()} {self.lastname.capitalize()}'
