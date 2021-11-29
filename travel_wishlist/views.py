from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
# Create your views here.

def place_list(request):

    if request.method =='POST':
        #create a new place
        form = NewPlaceForm(request.POST)
        place = form.save() #create a place object
        if form.is_valid():
            place.save()#save to the database
            return redirect('place_list') #reloads homepage from urls.py
    # places = Place.objects.all()
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html',{'places':places , 'new_place_form':new_place_form})

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request,'travel_wishlist/visited.html',{'visited':visited})

def about(request):
    author='Mo'
    about='A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html',{'author':author,'about':about})

def place_was_visited(request,place_pk):
    if request.method == 'POST':
        # place=Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place,pk=place_pk)
        place.visited = True
        place.save()
    return redirect('place_list')