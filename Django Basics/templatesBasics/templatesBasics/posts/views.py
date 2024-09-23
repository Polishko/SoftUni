from datetime import datetime
from lib2to3.fixes.fix_input import context

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
        'empty_text': '',
        'users': [
            'pesho',
            'maria',
            'ivan',
            'magdalena',
            'elisa',
        ]
    }

    return render(request, 'base.html', context)

def dashboard(request):
    context = {
        'posts':[
            {
                'title': 'How to create a Django project 1?',
                'author': 'Nalan',
                'content': 'I know a little about creating a Django project.',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create a Django project 2?',
                'author': 'Nalan',
                'content': 'I know a little about creating a Django project.',
                'created_at': datetime.now(),
            },
            {
                'title': 'How to create a Django project 3?',
                'author': 'Nalan',
                'content': 'I know a little about creating a Django project.',
                'created_at': datetime.now(),
            },

        ]
    }

    return render(request, 'posts/dashboard.html', context)