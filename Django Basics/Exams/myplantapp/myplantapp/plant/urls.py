from django.urls import path

from myplantapp.plant.views import PlantCreateView, PlantDetailView, PlantEditView, PlantDeleteView, PlantListView

urlpatterns = [
    path('create/', PlantCreateView.as_view(), name='plant-create'),
    path('catalogue/', PlantListView.as_view(), name='catalogue'),
    path('details/<int:plant_id>/', PlantDetailView.as_view(), name='plant-details'),
    path('edit/<int:plant_id>/', PlantEditView.as_view(), name='plant-edit'),
    path('delete/<int:plant_id>/', PlantDeleteView.as_view(), name='plant-delete'),
]
