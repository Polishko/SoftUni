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
        'ids': ['21348', '485769', '619074'],
        'some_text': 'hello, my name is Nalan, and I`m learning programming.',
        'empty_text': ''
    }

    return render(request, 'base.html', context)
