from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from tastyrecipes.userprofile.forms import ProfileCreateForm, ProfileEditForm
from tastyrecipes.userprofile.models import Profile
from tastyrecipes.utils import get_user_object


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'userprofile/create-profile.html'
    success_url = reverse_lazy('recipe_catalogue')

    def get_object(self, queryset=None):
        return get_user_object()


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'userprofile/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_object()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'userprofile/edit-profile.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_object()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'userprofile/delete-profile.html'
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return get_user_object()
