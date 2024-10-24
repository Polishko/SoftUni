from django.db import models


class CarTypeChoices(models.TextChoices):
    RALLY = 'rally', 'Rally'
    OPEN_WHEEL = 'open-wheel', 'Open-wheel'
    KART = 'kart', 'Kart'
    DRAG = 'drag', 'Drag'
    OTHER = 'Other', 'Other'

