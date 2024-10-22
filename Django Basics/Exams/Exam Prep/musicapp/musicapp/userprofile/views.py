from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from musicapp.userprofile.models import Profile
from musicapp.utils import get_user_object


class ProfileDetails(DetailView):
    model = Profile
    template_name = 'userprofile/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_object()

class ProfileDelete(DeleteView):
    model = Profile #optional because we override get_object but better for readability
    template_name = 'userprofile/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_user_object()

