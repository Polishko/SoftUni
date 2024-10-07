from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect, get_object_or_404

from Petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from Petstagram.pets.models import Pet


# Create your views here.

def pet_add_page(request):
    form = PetCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form}

    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    # pet = get_object_or_404(Pet, slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_edit_page(request, username: str, pet_slug: str):
    pet = get_object_or_404(Pet, slug=pet_slug)
    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    # if request.method == 'GET':
    #     # form = PetEditForm(instance=pet, initial=pet.__dict__)
    #     form = PetEditForm(instance=pet)
    # else:
    #     form = PetEditForm(request.POST, instance=pet)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('pet-details', username, pet_slug)

    context = {'form': form}

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def pet_delete_page(request, username: str, pet_slug: str):
    pet = get_object_or_404(Pet, slug=pet_slug)
    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-delete-page.html', context=context)
