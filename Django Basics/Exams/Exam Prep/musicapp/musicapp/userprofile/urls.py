from django.urls import path
from musicapp.userprofile.views import ProfileDetails, ProfileDelete

urlpatterns = [
    path('details/', ProfileDetails.as_view(), name='profile-details'),
    path('delete/', ProfileDelete.as_view(), name='profile-delete'),
]
