from django.urls import path, include

from Petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details, name='pet-details'),
        path('', views.edit_pet, name='edit_pet'),
        path('', views.delete_pet, name='delete_pet'),
    ]))
]