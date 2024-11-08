from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify


UserModel = get_user_model()


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    # slug goes to url and therefore should be unique, un-editable (admin, form)
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        editable=False,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        # Call super().save(*args, **kwargs) before the slugify logic to ensure
        # that the object is saved to the database first,
        # so that it has a valid primary key (self.pk).
        super().save(*args, **kwargs)

        # keep slug when pet name changes
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name