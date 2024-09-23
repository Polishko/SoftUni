from django.urls import path

from templatesBasics.posts.views import index


urlpatterns = [
    path('', index, name='index'),
]