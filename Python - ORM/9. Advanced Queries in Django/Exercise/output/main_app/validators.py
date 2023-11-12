from django.core.exceptions import ValidationError
from decimal import Decimal


def validate_rate(value):
    if Decimal(value) < 0.0 or Decimal(value) > 10.0:
        raise ValidationError("The rating must be between 0.0 and 10.0")


def validate_release_year(value):
    if value < 1990 or value > 2023:
        raise ValidationError("The release year must be between 1990 and 2023")
