from django.urls import include, path

from fruitipedia.fruit.views import FruitCreateView, FruitDetailView, FruitEditView, FruitDeleteView

urlpatterns = [
    path('create/', FruitCreateView.as_view(), name='fruit-create'),
    path('<int:fruitId>/', include([
        path('details/', FruitDetailView.as_view(), name='fruit-details'),
        path('edit/', FruitEditView.as_view(), name='fruit-edit'),
        path('delete/', FruitDeleteView.as_view(), name='fruit-delete'),
    ]))
]
