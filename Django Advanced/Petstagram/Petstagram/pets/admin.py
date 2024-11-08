from django.contrib import admin

from Petstagram.pets.models import Pet
from Petstagram.photos.models import Photo


# Register your models here.
@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'description', 'get_tagged_pets')

    # Django admin passes the instance automatically so self not needed
    @staticmethod
    def get_tagged_pets(photo_obj):
        return ', '.join([pet.name for pet in photo_obj.tagged_pets.all()])

