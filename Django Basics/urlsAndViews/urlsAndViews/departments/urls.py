from django.urls import path
from urlsAndViews.departments import views


urlpatterns = [
    path('', views.index),
    path('<param>/', views.view_with_name),
]


