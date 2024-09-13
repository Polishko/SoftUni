from django.urls import path
from djangoIntroduction.todo_app.views import index

urlpatterns = [
    path('', index, name='index'),
]