from django.contrib import admin

from musicapp.album.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass