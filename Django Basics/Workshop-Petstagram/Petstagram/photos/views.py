from django.shortcuts import render

# Create your views here.
def add_photo(request):
    return render(request, template_name='photos/photo-add-page.html')

def photo_details(request):
    return render(request, template_name='photos/photo-details-page.html')

def edit_photo(request):
    return render(request, template_name='photos/photo-edit-page.html')
