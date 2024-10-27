from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models

from furryfunnies.userprofile.validators import NameValidator, PassCodeValidator


class Author(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=40,
        validators=(
            MinLengthValidator(4),
            NameValidator(),
        ),
        verbose_name='First Name',
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        validators=(
            MinLengthValidator(2),
            NameValidator(),
        ),
        verbose_name='Last Name',
    )

    passcode = models.CharField(
        null=False,
        blank=False,
        max_length=6,
        validators=(
            PassCodeValidator(),
        ),
        help_text='Your passcode must be a combination of 6 digits',
        verbose_name='Passcode',
    )

    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        verbose_name='Pets Number',
    )

    info = models.TextField(
        null=True,
        blank=True,
        verbose_name='Info',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

    def get_full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
