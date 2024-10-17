from django.urls import path

from musicapp.common.views import show_home

urlpatterns = [
    path('', show_home, name='home-page')
]