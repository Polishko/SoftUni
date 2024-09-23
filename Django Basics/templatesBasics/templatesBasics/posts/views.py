from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def  index(request):
    context = {
        'current_time': datetime.now(),
        'person': {
            'age': 46,
            'height': 160,
        },
        'ids': ['21348', '485769', '619074']
    }

    return render(request, 'base.html', context)
