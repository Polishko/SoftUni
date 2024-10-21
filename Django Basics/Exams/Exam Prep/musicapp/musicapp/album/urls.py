
from django.urls import path, include

from musicapp.album.views import AddAlbum, AlbumDetails, AlbumEdit, AlbumDelete

urlpatterns = [
    path('add/', AddAlbum.as_view(), name='album-add'),
    path('<int:pk>/', include([
        path('details/', AlbumDetails.as_view(), name='album-details'),
        path('edit/', AlbumEdit.as_view(), name='album-edit'),
        path('delete/', AlbumDelete.as_view(), name='album-delete'),
    ]))
]
