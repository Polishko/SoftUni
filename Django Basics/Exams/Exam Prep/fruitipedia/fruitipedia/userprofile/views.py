from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia.userprofile.forms import ProfileCreateForm, ProfileEditForm
from fruitipedia.userprofile.models import Profile
from fruitipedia.utils import get_user_object


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'userprofile/create-profile.html'
    success_url = reverse_lazy('dashboard')
    form_class = ProfileCreateForm


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'userprofile/details-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_user_object()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'userprofile/edit-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return get_user_object()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'userprofile/delete-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return get_user_object()
