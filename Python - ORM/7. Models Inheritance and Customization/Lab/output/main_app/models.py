from datetime import date, timedelta

from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Animal(models.Model):
    name = models.CharField(
        max_length=100
    )
    species = models.CharField(
        max_length=100
    )
    birth_date = models.DateField()
    sound = models.CharField(
        max_length=100
    )

    @property
    def age(self):
        today = date.today()
        years = today.year - self.birth_date.year

        if ((today.month < self.birth_date.month)
                or (today.month == self.birth_date.month and today.day < self.birth_date.day)):
            years -= 1

        return years


class Mammal(Animal):
    fur_color = models.CharField(
        max_length=50
    )


class Bird(Animal):
    wing_span = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )


class Reptile(Animal):
    scale_type = models.CharField(
        max_length=50
    )


class Employee(models.Model):
    first_name = models.CharField(
        max_length=50
    )
    last_name = models.CharField(
        max_length=50
    )
    phone_number = models.CharField(
        max_length=10
    )

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    SPECIALIZATION = [
        ("Mammals", "Mammals"),
        ("Birds", "Birds"),
        ("Reptiles", "Reptiles"),
        ("Others", "Others")
    ]

    specialty = models.CharField(
        max_length=10,
        choices=SPECIALIZATION
    )
    managed_animals = models.ManyToManyField(
        Animal
    )

    def clean(self):

        if self.specialty not in dict(self.SPECIALIZATION):
            raise ValidationError("Specialty must be a valid choice.")


class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs["choices"] = [
            (True, "Available"),
            (False, "Not Available")
        ]
        kwargs["default"] = True
        super().__init__(*args, **kwargs)


class Veterinarian(Employee):
    license_number = models.CharField(
        max_length=10
    )
    availability = BooleanChoiceField()

    def is_available(self):
        return self.availability


class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    def display_info(self):
        extra_info = ""

        if hasattr(self, "mammal"):
            extra_info = f" Its fur color is {self.mammal.fur_color}."
        elif hasattr(self, "bird"):
            extra_info = f" Its wingspan is {self.bird.wing_span} cm."
        elif hasattr(self, "reptile"):
            extra_info = f" Its scale type is {self.reptile.scale_type}."

        return (f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}."
                f" It makes a noise like '{self.sound}'!{extra_info}")

    def is_endangered(self):
        if self.species in ["Cross River Gorilla", "Orangutan", "Green Turtle"]:
            return True

        return False
