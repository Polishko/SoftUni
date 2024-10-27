from django.urls import path

from furryfunnies.userprofile.views import AuthorCreateView, AuthorDetailView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='author-create'),
    path('details/', AuthorDetailView.as_view(), name='author-detail'),
    path('edit/', AuthorEditView.as_view(), name='author-edit'),
    path('delete/', AuthorDeleteView.as_view(), name='author-delete'),
]
