from django.urls import path

from fruitipedia.common.views import show_index, show_dashboard

urlpatterns = [
    path('', show_index, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
]