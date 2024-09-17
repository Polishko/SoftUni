from django.urls import path
from urlsAndViews.departments import views


urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.view_with_int_pk),
    path('<param>/', views.view_with_name),
]


