from django.shortcuts import render

from Petstagram.pets.models import Pet
from Petstagram.photos.models import Photo


# Create your views here.
def pet_add_page(request):
    return render(request, template_name='pets/pet-add-page.html')

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
    return render(request, template_name='pets/pet-edit-page.html')

def pet_delete_page(request, username: str, pet_slug: str):
    return render(request, template_name='pets/pet-delete-page.html')
