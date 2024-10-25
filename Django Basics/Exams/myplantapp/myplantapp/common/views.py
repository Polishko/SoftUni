from django.shortcuts import render
from django.views.generic import ListView

from myplantapp.plant.models import Plant


def show_home_page(request):
    return render(request, 'common/home-page.html')
