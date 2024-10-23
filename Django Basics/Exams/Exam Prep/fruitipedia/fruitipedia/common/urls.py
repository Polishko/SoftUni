from django.urls import path

from fruitipedia.common.views import show_index, DashboardView

urlpatterns = [
    path('', show_index, name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]