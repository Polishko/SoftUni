from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CharField, ImageField, TextField, FloatField, ForeignKey, CASCADE, URLField

from myplantapp.plant.choices import PlantTypeChoices
from myplantapp.plant.validators import PlantNameValidator


class Plant(models.Model):
    type = CharField(
        null=False,
        blank=False,
        max_length=14,
        choices = PlantTypeChoices.choices,
        verbose_name='Type',
    )

    name = CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            MinLengthValidator(2),
            PlantNameValidator(),
        ),
        verbose_name='Name',
    )

    image_url = URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    description = TextField(
        null=False,
        blank=False,
        verbose_name='Description',
    )

    price = FloatField(
        null=False,
        blank=False,
    )

    owner = ForeignKey(
        to='userprofile.Profile',
        on_delete=CASCADE,
        related_name='plants',
    )