from django.db import models

class GenreChoices(models.TextChoices):
    POP_MUSIC = 'pop', 'Pop Music'
    JAZZ_MUSIC = 'jazz', 'Jazz Music'
    RB_MUSIC = 'rb', 'R&B Music'
    ROCK_MUSIC = 'rock', 'Rock Music'
    COUNTRY_MUSIC = 'country', 'Country Music'
    DANCE_MUSIC = 'dance', 'Dance Music'
    HIP_HOP_MUSIC = 'hiphop', 'Hip Hop Music'
    OTHER = 'other', 'Other'

