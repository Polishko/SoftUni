from django.urls import path
from urlsAndViews.departments import views


urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.view_with_int_pk),
    path('<int:pk>/<slug:slug>', views.view_with_slug),
    path('<param>/', views.view_with_name),
]


