from django.contrib import admin
from .models import AboutPage, Hyperlinks, Archivements, InquiryDetails, Gallery

class Service(admin.ModelAdmin):
    list_display= (
        'name',
        'img',
        'title',
        'experience',
        'email',
        'bio',
        'paragraph_title',
        'paragraph_description'
    )

# Register your models here.
admin.site.register(AboutPage, Service)
admin.site.register(InquiryDetails)
admin.site.register(Archivements)
admin.site.register(Hyperlinks)
admin.site.register(Gallery)
