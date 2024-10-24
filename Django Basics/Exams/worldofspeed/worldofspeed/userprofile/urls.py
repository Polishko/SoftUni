from django.urls import path

from worldofspeed.userprofile.views import ProfileCreateView, ProfileDetailView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile-create'),
    path('details/', ProfileDetailView.as_view(), name='profile-detail'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]
