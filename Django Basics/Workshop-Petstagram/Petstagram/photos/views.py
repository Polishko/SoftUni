from django.shortcuts import render

# Create your views here.
def photo_add_page(request):
    return render(request, template_name='photos/photo-add-page.html')

def photo_details_page(request, pk: int):
    return render(request, template_name='photos/photo-details-page.html')

def photo_edit_page(request, pk: int):
    return render(request, template_name='photos/photo-edit-page.html')
