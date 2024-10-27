from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import CASCADE


class Post(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=50,
        validators=(
            MinLengthValidator(5),
        ),
        error_messages={
            'unique': 'Oops! That title is already taken. How about something fresh and fun?'
        },
        verbose_name='Title',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        help_text='Share your funniest furry photo URL!',
        verbose_name='Post Image URL',
    )

    content = models.TextField(
        null=False,
        blank=False,
        verbose_name='Content'
    )

    updated_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now=True,
    )

    author = models.ForeignKey(
        to='userprofile.Author',
        on_delete=CASCADE,
    )
