from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Petstagram.common.forms import CommentForm
from Petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet


class AddPetView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'
    # success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    success_url = reverse_lazy('profile-details')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        # pet.save()
        return super().form_valid(form) # pet saved here

    # no need, we removed pk from search params
    # def get_success_url(self):
    #     return reverse_lazy(
    #         'profile-details',
    #         kwargs={'pk': self.request.user.pk}
    #     )

class PetDetailView(LoginRequiredMixin, DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug' # otherwise searches for slug

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all() # we can use context['pet'] too
        context['comment_form'] = CommentForm()
        return context


class PetEditView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    # context_object_name = 'pet' # no need, inferred from model name

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username':self.kwargs['username'],
                'pet_slug':self.object.slug, # or self.kwargs['pet_slug']
            }
        )

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model =Pet
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    # no need for form_class, we don't use form to submit user input

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(instance=self.object)
        return context

    # no need, Django will remove the tagged pet from the photos
    # def delete(self, request, *args, **kwargs):
    #     pet_object = self.get_object()
    #
    #     related_photos = Photo.objects.filter(tagged_pets=pet_object)
    #     for photo in related_photos:
    #         photo.tagged_pets.remove(pet_object)
    #
    #     return super().delete(request, *args, **kwargs)



