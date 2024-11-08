from lib2to3.fixes.fix_input import context

from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from Petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from Petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    # model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    # success_url = reverse_lazy('login')

    # Let`s log the user immediately after they have registered
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form) # validate and save user
        login(self.request, self.object) # log user

        return response


class AppUserLoginView(LoginView):
    # form_class = AppUserLoginForm # removed since we directly login on register
    template_name = 'accounts/login-page.html'
    # success_url = reverse_lazy('home')


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    # since removed the id from path for security we need to get object explicitly
    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            # kwargs={'pk': self.object.pk}
        )


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # since profile obj has reverse relation with user can access photos
        photos_with_likes = self.request.user.photo_set.annotate(likes_count=Count('likes')) # single join
        context['total_likes'] = sum(photo.likes_count for photo in photos_with_likes)
        # context['total_likes'] = self.object.photo_set.prefetch_related('likes')

        context['total_pets'] = self.request.user.pet_set.count()
        context['total_photos'] = self.request.user.photo_set.count()

        return context

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user.profile

