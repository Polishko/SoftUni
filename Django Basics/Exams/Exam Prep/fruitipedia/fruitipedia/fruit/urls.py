from django.urls import include, path

from fruitipedia.fruit.views import fruit_create, fruit_details, fruit_edit, fruit_delete

urlpatterns = [
    path('create/', fruit_create, name='fruit-create'),
    path('<int:fruitId>/', include([
        path('details/', fruit_details, name='fruit-details'),
        path('edit/', fruit_edit, name='fruit-edit'),
        path('delete/', fruit_delete, name='fruit-delete'),
    ]))
]
