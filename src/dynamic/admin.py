from django.contrib import admin
from .models import AboutPage, Hyperlink, Achivement, InquiryDetail, Gallery

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
admin.site.register(InquiryDetail)
admin.site.register(Achivement)
admin.site.register(Hyperlink)
admin.site.register(Gallery)
