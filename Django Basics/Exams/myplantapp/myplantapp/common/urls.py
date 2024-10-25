from django.urls import path

from myplantapp.common.views import show_home_page


urlpatterns = [
    path('', show_home_page, name='home'),
]