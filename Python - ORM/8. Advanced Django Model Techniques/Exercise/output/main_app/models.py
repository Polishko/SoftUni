from decimal import Decimal

from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MinLengthValidator


# Create your models here.
# 1. Customer
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z\s]+$",
                message="Name can only contain letters and spaces"
            )
        ]
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                18,
                "Age must be greater than 18"
            )
        ]
    )
    email = models.EmailField()
    # if you want custom message:
    EmailField(error_messages="invalid": {"custom message"})
    
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^\+359[\d]{9}$",
                message="Phone number must start with a '+359' followed by 9 digits"
            )
        ]
    )
    #or use a re.match(regex_pattern) in a separate function kept in separate file for validators
    
    website_url = models.URLField()
    # if you want custom message:
    URLField(error_messages="invalid": {"custom message"})


# 2.	Media
class BaseMedia(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    genre = models.CharField(
        max_length=50
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True
        ordering = ["-created_at", "title"]


class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                5, "Author must be at least 5 characters long"
            )
        ]
    )

    isbn = models.CharField(
        max_length=6,
        unique=True,
        validators=[
            MinLengthValidator(
                6, "ISBN must be at least 6 characters long"
            )
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"


class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                8, "Director must be at least 8 characters long"
            )
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"


class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                9, "Artist must be at least 9 characters long"
            )
        ]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"


# 3.	Digital Products
class Product(models.Model):
    name = models.CharField(
        max_length=100
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def calculate_tax(self):
        return self.price * Decimal(0.08)

    @staticmethod
    def calculate_shipping_cost(weight: Decimal):
        return weight * Decimal(2.00)

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    def calculate_price_without_discount(self):
        return self.price * Decimal(1.20)

    def calculate_tax(self):
        return self.price * Decimal(0.05)

    @staticmethod
    def calculate_shipping_cost(weight: Decimal):
        return weight * Decimal(1.5)

    def format_product_name(self):
        return f"Discounted Product: {self.name}"

    class Meta:
        proxy = True


# 4.	Superhero Universe
class RechargeEnergyMixin(models.Model):
    energy = models.PositiveIntegerField()

    def recharge_energy(self, amount: int):
        final_energy = self.energy + amount

        self.energy = min(100, final_energy)


class Hero(RechargeEnergyMixin):
    name = models.CharField(
        max_length=100
    )
    hero_title = models.CharField(
        max_length=100
    )


class SpiderHero(Hero):
    def swing_from_buildings(self):
        self.energy -= 80

        if self.energy <= 0:
            return f"{self.name} as Spider Hero is out of web shooter fluid"

        self.save()
        return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:
        proxy = True


class FlashHero(Hero):
    def run_at_super_speed(self):
        self.energy -= 65

        if self.energy <= 0:
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.save()
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:
        proxy = True
