from django.contrib.auth import get_user, get_user_model
from django.db import models

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel ,
        on_delete=models.CASCADE,
        primary_key=True, # id is the id of user, avoids creating extra id field
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def get_profile_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name or self.last_name:
            return {self.first_name} or {self.last_name}
        else:
            return 'Anonymous User'
