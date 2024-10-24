from django.urls import path, include

from worldofspeed.car.views import CarCreateView, CarEditView, CarDetailView, CarDeleteView, CarListView


urlpatterns = [
    path('catalogue/', CarListView.as_view(), name='car-catalogue'),
    path('create/', CarCreateView.as_view(), name='car-create'),
    path('<int:id>/', include([
        path('details/', CarDetailView.as_view(), name='car-detail'),
        path('edit/', CarEditView.as_view(), name='car-edit'),
        path('delete/', CarDeleteView.as_view(), name='car-delete'),
    ]))
]