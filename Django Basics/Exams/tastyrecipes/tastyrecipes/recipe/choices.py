
from django.db import models


class RecipeTypeChoices(models.TextChoices):
    FRENCH = 'french', 'French'
    CHINESE = 'chinese', 'Chinese'
    ITALIAN = 'italian', 'Italian'
    BALKAN = 'balkan', 'Balkan'
    OTHER ='other', 'Other'
