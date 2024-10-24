from django.urls import path

from worldofspeed.common.views import show_index

urlpatterns = [
    path('', show_index, name='index')
]