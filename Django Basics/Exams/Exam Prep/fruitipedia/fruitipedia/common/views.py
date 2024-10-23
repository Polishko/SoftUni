from django.shortcuts import render
from django.views.generic import ListView

from fruitipedia.fruit.models import Fruit


def show_index(request):
    return render(request, 'common/index.html')

class DashboardView(ListView):
    model = Fruit
    context_object_name = 'fruits'
    template_name = 'common/dashboard.html'
