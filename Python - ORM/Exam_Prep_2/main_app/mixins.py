from django.db import models


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True


class CreationMixin(models.Model):
    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        abstract = True


class IsAvailableMixin(models.Model):
    is_available = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True


class IsCompletedMixin(models.Model):
    is_completed = models.BooleanField(
        default=False
    )

    class Meta:
        abstract = True
