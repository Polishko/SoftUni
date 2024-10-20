from django.urls import path

from musicapp.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page')
]