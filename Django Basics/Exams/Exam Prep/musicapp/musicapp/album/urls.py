
from django.urls import path, include
from musicapp.album.views import album_add, album_edit, album_details, album_delete

urlpatterns = [
    path('add/', album_add, name='album-add'),
    path('<int:pk>', include([
        path('details/', album_details, name='album-details'),
        path('edit/', album_edit, name='album-edit'),
        path('delete/', album_delete, name='album-delete'),
    ]))
]
