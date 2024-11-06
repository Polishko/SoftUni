from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# _ allows translation to other languages
from django.utils.translation import gettext_lazy as _

from forumApp.accounts.managers import AppUserManager


# class CustomUser(AbstractUser):
#     points = models.IntegerField(
#         default=0,
#     )

class AppUser(AbstractBaseUser, PermissionsMixin):
    # Added these because we already wrote a backend that uses emain and username for auth
    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    # The below are important to have for admin, so we copied these from AbstractUser
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    # Add your manager (custom: inheriting from BaseUserManager)
    objects = AppUserManager()

    # Add the main credential for login
    USERNAME_FIELD = 'email'

    # Add to tell Django what to use to send account related emails
    EMAIL_FIELD = 'email'

    # Add required fields so that user doesn't just login with password
    REQUIRED_FIELDS = ['username']

    # For representation purposes
    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(
        # to=CustomUser,
        to=AppUser,
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
