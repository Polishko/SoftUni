from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE

from fruitipedia.userprofile.validators import FruitNameValidator


class Fruit(models.Model):
    fruit_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
        validators=(
            MinLengthValidator(2),
            FruitNameValidator(),
        ),
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.',
        },
        verbose_name='Fruit Name',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Description',
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
        verbose_name='Nutrition',
    )

    owner = models.ForeignKey(
        to='userprofile.Profile',
        on_delete=CASCADE,
        null=False,
        blank=True,  # maybe not needed
        related_name= 'fruits',
    )
