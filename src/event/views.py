from django.shortcuts import render, get_object_or_404, get_list_or_404
import datetime
from .models import Events
from src.dynamic.models import Gallery

# Fetcg all the gallery images
gallery_images  = Gallery.objects.all().values_list('gallery_image', flat=True).distinct()

def home_view(request):
    events = Events.objects.all()

    date = request.GET.get('eventDate', '')
    if date != '':
        date = datetime.datetime.strptime(request.GET.get('eventDate', ''), '%m/%d/%Y').date()
        print(date)
    search = request.GET.get('search', '')

    if (date != '' and search):
        pass
    elif (search):
        events = events.filter(title__icontains=search)
    elif (date != ''):
        events = events.filter(date__icontains=date)


    return render(request, 'event/events.html', {
        'events': events,
        'dateValue': date,
        'searchValue': search,
        'images': gallery_images
    })

def eventDetails_view(request, slug):
    obj = get_object_or_404(Events, slug=slug)
    return render(request, 'event/details.html', {
        'event': obj,
        'events': get_list_or_404(Events), 
        'images': gallery_images,
    })