from django.urls import path, include

from Petstagram.photos import views

urlpatterns = [
    path('add/', views.PhotoCreateView.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailView.as_view(), name='photo-details'),
        path('edit/', views.PhotoEditView.as_view(), name='photo-edit'),
        path('delete/', views.delete_photo, name='photo-delete'),
    ])),
]
