from django.urls import include, path

from fruitipedia.userprofile.views import profile_create, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('create/', profile_create, 'profile-create'),
    path('', include([
        path('details/', profile_details, 'profile-details'),
        path('edit/', profile_edit, 'profile-edit'),
        path('delete/', profile_delete, 'profile-delete'),
    ]))
]
