from django.shortcuts import render, get_object_or_404

from Petstagram.photos.models import Photo


# Create your views here.
def photo_add_page(request):
    return render(request, template_name='photos/photo-add-page.html')

def photo_details_page(request, pk: int):
    photo = get_object_or_404(Photo, pk=pk)
    comments = photo.comment_set.all()
    likes = photo.like_set.all()

    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)

def photo_edit_page(request, pk: int):
    return render(request, template_name='photos/photo-edit-page.html')

def photo_delete_page(request, pk: int):
    return render(request, template_name='photos/photo-delete-page.html')
