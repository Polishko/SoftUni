from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Petstagram.common.forms import CommentForm
from Petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet
from Petstagram.photos.models import Photo


class AddPetView(CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


class PetDetailView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm()
        return context


class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username':self.kwargs['username'],
                'pet_slug':self.object.slug,
            }
        )

class PetDeleteView(DeleteView):
    model =Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(instance=self.object)
        return context

    def delete(self, request, *args, **kwargs):
        pet_object = self.get_object()

        related_photos = Photo.objects.filter(tagged_pets=pet_object)
        for photo in related_photos:
            photo.tagged_pets.remove(pet_object)

        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': 1,
            }
        )


