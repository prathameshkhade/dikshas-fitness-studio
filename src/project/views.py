from django.shortcuts import render

from src.dynamic.models import AboutPage, Archivements, Hyperlinks
from src.classes.models import ClassInfo

# Create your views here
def homepage_view(request): 
    tdata = ClassInfo().getdata()
    data = { 'data': tdata }
    print(data) 

    return render(request, "home.html", data)

def contact_view(request):  
    return render(request, "contact.html")

def about_view(request):  
    table_data = AboutPage.objects.get(id=1)

    data = {
        'image': table_data.img,
        'name': table_data.name,
        'title': table_data.title,
        'experience': table_data.experience,
        'email': table_data.email,
        'bio': table_data.bio,
        'paragraph_title': table_data.paragraph_title,
        'paragraph_description': table_data.paragraph_description
    }
    
    # adding archivements from table to website
    data['archivements'] = [
        x.archivements for x in Archivements.objects.all()
    ]

    # addinng hyperlinks in data
    data['hyperlinks'] = Hyperlinks().getdata()

    return render(request, "about.html", data)


def classes_view(request): 
    tdata = ClassInfo().getdata()
    data = { 'data': tdata }
    print(data)

    return render(request, "classes.html", data)
