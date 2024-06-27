from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Events

def home_view(request):
    events_objects = Events.objects.all()
    print(events_objects)
    return render(request, 'event/events.html', {
        'events': events_objects
    })

def eventDetails_view(request, slug):
    obj = Events.objects.get(slug = slug)
    return render(request, 'event/details.html', {
        'event': obj
    })