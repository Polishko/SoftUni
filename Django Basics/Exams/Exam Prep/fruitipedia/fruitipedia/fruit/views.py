from django.shortcuts import render

def fruit_create(request):
    return render(request, 'fruit/create-fruit.html')

def fruit_details(request, fruitId):
    return render(request, 'fruit/details-fruit.html')

def fruit_edit(request, fruitId):
    return render(request, 'fruit/edit-fruit.html')

def fruit_delete(request, fruitId):
    return render(request, 'fruit/delete-fruit.html')
