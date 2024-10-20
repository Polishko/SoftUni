
from django.urls import path, include
from musicapp.album.views import album_edit, album_details, album_delete, AddAlbum, AlbumDetails

urlpatterns = [
    path('add/', AddAlbum.as_view(), name='album-add'),
    path('<int:pk>/', include([
        path('details/', AlbumDetails.as_view(), name='album-details'),
        path('edit/', album_edit, name='album-edit'),
        path('delete/', album_delete, name='album-delete'),
    ]))
]
