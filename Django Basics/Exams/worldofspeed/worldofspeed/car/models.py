from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import CASCADE

from worldofspeed.car.choices import CarTypeChoices
from worldofspeed.userprofile.validators import CarYearValidator


class Car(models.Model):
    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=CarTypeChoices.choices,
        verbose_name='Type',
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(
            MinLengthValidator(1),
        ),
        verbose_name='Model',
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            CarYearValidator(),
        ),
        verbose_name='Year',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(1.0),
        ),
        verbose_name='Price',
    )

    owner = models.ForeignKey(
        to='userprofile.Profile',
        on_delete=CASCADE,
        null=False,
        related_name='cars',
    )
