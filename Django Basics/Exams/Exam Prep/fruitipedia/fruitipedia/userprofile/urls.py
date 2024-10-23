from django.urls import include, path

from fruitipedia.userprofile.views import (ProfileCreateView, ProfileDetailView, ProfileEditView,
                                           ProfileDeleteView)

urlpatterns = [
    path('', include([
        path('create/', ProfileCreateView.as_view(), name='profile-create'),
        path('details/', ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]
