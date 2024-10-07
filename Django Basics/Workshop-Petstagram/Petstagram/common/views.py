from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy


from Petstagram.common.models import Like
from Petstagram.photos.models import Photo


# Create your views here.
def show_home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'photos': all_photos
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    # Better: photo = get_object_or_404(Photo, pk=photo_id)
    liked_object = Like.objects.filter(to_photo=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect((request.META['HTTP_REFERER']) + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    # Get the full URL of the photo
    full_url = f"{request.META['HTTP_HOST']}{resolve_url('photo-details', photo_id)}"

    # Use pyperclip to copy to the clipboard (or another clipboard library you're using)
    copy(full_url)

    # Redirect back to the previous page
    return redirect(f"{request.META.get('HTTP_REFERER', '/')}#{photo_id}")
