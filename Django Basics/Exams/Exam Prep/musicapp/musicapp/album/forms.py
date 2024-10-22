from django import forms

from musicapp.mixins import PlaceholderMixin, ReadOnlyMixin
from musicapp.album.models import Album

class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class AddAlbumForm(PlaceholderMixin, AlbumBaseForm):
    pass


class EditAlbumForm(PlaceholderMixin, AlbumBaseForm):
    pass


class DeleteAlbumForm(ReadOnlyMixin, AlbumBaseForm):
    readonly_fields = ['album_name', 'artist', 'genre', 'price', 'description']
