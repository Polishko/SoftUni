from django.urls import path
from musicapp.userprofile.views import profile_delete, UserDetails

urlpatterns = [
    path('details/', UserDetails.as_view(), name='profile-details'),
    path('delete/', profile_delete, name='profile-delete'),
]
