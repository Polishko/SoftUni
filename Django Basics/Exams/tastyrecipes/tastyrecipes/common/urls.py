from django.urls import path

from tastyrecipes.common.views import show_homepage

urlpatterns = [
    path('', show_homepage, name='home_page'),
]
