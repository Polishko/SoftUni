from django import forms
from musicapp.album.models import Album

class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }

class AddAlbumForm(AlbumBaseForm):
    pass


class EditAlbumForm(AlbumBaseForm):
    pass

class DeleteAlbumForm(AlbumBaseForm):
    pass
