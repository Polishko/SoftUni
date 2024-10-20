
from django.urls import path, include

from musicapp.album.forms import EditAlbumForm
from musicapp.album.views import album_delete, AddAlbum, AlbumDetails, AlbumEdit

urlpatterns = [
    path('add/', AddAlbum.as_view(), name='album-add'),
    path('<int:pk>/', include([
        path('details/', AlbumDetails.as_view(), name='album-details'),
        path('edit/', AlbumEdit.as_view(), name='album-edit'),
        path('delete/', album_delete, name='album-delete'),
    ]))
]
