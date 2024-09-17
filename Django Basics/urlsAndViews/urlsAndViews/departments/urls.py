from django.urls import path
from urlsAndViews.departments.views import index


urlpatterns = [
    path('', index),
]
