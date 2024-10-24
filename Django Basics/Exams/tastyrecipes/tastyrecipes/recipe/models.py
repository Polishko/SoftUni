from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import CharField, TextField, PositiveIntegerField, URLField, ForeignKey, CASCADE

from tastyrecipes.recipe.choices import RecipeTypeChoices


class Recipe(models.Model):
    title = CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=100,
        validators=(
            MinLengthValidator(10),
        ),
        verbose_name='Title',
    )

    cuisine_type = CharField(
        choices=RecipeTypeChoices.choices,
        null=False,
        blank=False,
        max_length=7,
        verbose_name='Cuisine Type',
    )

    ingredients = TextField(
        null=False,
        blank=False,
        help_text='Ingredients must be separated by a comma and space.',
        verbose_name='Ingredients',
    )

    instructions = TextField(
        null=False,
        blank=False,
        verbose_name='Instructions',
    )

    cooking_time = PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(1),
        ),
        help_text='Provide the cooking time in minutes.',
        verbose_name='Cooking Time'
    )

    image_url = URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

    author = ForeignKey(
        to='userprofile.Profile',
        on_delete=CASCADE,
        null=False,
        related_name='recipes',
        verbose_name='Author'
    )
