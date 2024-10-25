from django.db import models


class PlantTypeChoices(models.TextChoices):
    OUTDOOR_PLANTS = 'Outdoor', 'Outdoor'
    INDOOR_PLANTS = 'Indoor', 'Indoor Plants'
