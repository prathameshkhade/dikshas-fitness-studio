from django.contrib import admin
from .models import AboutPage, Hyperlinks, Archivements

class Service(admin.ModelAdmin):
    list_display= (
        # 'image',
        'name',
        'title',
        'experience',
        'email',
        'bio',
        'paragraph_title',
        'paragraph_description'
    )

# Register your models here.
admin.site.register(AboutPage, Service)
admin.site.register(Archivements)
admin.site.register(Hyperlinks)
