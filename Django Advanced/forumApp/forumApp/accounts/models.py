from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    points = models.IntegerField(
        default=0,
    )


class Profile(models.Model):
    user = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE,
    )

    age = models.IntegerField()

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    points = models.IntegerField(
        default=0,
    )
