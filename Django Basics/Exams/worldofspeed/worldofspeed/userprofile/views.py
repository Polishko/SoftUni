from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from worldofspeed.userprofile.forms import ProfileCreateForm, ProfileEditForm
from worldofspeed.userprofile.models import Profile
from worldofspeed.utils import get_user_object


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'userprofile/profile-create.html'
    success_url = reverse_lazy('car-catalogue')
    form_class = ProfileCreateForm


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'userprofile/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_cars = self.object.cars
        total_price = sum(car.price for car in all_cars.all())
        context['total_price'] = total_price

        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'userprofile/profile-edit.html'
    success_url = reverse_lazy('profile-detail')

    def get_object(self, queryset=None):
        return get_user_object()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'userprofile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_object()
