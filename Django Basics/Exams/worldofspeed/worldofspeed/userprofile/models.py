from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldofspeed.userprofile.validators import UserNameValidator


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(
            MinLengthValidator(3),
            UserNameValidator(),
        ),
        verbose_name='Username'
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(21, message='Age must be at least 21!'),
        ),
        help_text='Age requirement: 21 years and above.',
        verbose_name='Age',
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        verbose_name='Password'
    )

    firstname = models.CharField(
        blank=True,
        null=True,
        max_length=25,
        verbose_name='First Name'
    )

    lastname = models.CharField(
        blank=True,
        null=True,
        max_length=25,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )

    def get_full_name(self):
        if self.firstname and self.lastname:
            return f'{self.firstname} {self.lastname}'
        elif self.firstname:
            return f'{self.firstname}'
        elif self.lastname:
            return f'{self.lastname}'
        return None