from django.shortcuts import render

# Create your views here.
def show_home(request):
    context = {}
    return render(request, 'common/home-page.html')




