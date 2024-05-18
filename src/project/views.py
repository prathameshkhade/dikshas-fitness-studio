from django.shortcuts import render
from django.http import JsonResponse

from src.dynamic.models import AboutPage, Archivements, Hyperlinks, InquiryDetails, Gallery
from src.classes.models import ClassInfo

# Fetcg all the gallery images
gallery_images  = Gallery.objects.all().values_list('gallery_image', flat=True).distinct()

# Create your views here
def homepage_view(request): 
    tdata = ClassInfo().getdata()
    data = { 'data': tdata }

    data['images'] = gallery_images

    return render(request, "home.html", data)

def contact_view(request):  
    data = {}
    
    data['images'] = gallery_images

    return render(request, "contact.html", data)

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

    # adding images to data
    data['images'] = gallery_images

    return render(request, "about.html", data)


def classes_view(request): 
    tdata = ClassInfo().getdata()
    data = { 'data': tdata }

    data['images'] = gallery_images

    return render(request, "classes.html", data)

def save(request):
    saved = False

    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        desc = request.POST.get('desc')

        obj = InquiryDetails(fname=fname, lname=lname, email=email, mobile=mob, description=desc)
        obj.save()

        saved = True

    return  JsonResponse({'success': saved})
