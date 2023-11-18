from django.db import models
from main_app.mixins import IsActiveMixin, CreationMixin, IsAvailableMixin, IsCompletedMixin
from django.core.validators import MinLengthValidator, MinValueValidator
from main_app.managers import ProfileManager


# Create your models here.
class Profile(IsActiveMixin, CreationMixin):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2)
        ]
    )
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15
    )
    address = models.TextField()
    objects = ProfileManager()


class Product(IsAvailableMixin, CreationMixin):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01)
        ]
    )
    in_stock = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )


class Order(CreationMixin, IsCompletedMixin):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="profile_orders"
    )
    products = models.ManyToManyField(
        to=Product,
        related_name="product_in_orders"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01)
        ]
    )
