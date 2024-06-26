from django.shortcuts import render

def home_view(request):
    return render(request, 'event/events.html')
