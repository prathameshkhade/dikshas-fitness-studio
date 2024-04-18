from django.contrib import admin
from .models import AboutPage

class Service(admin.ModelAdmin):
    list_display= (
        'name',
        'title',
        'experience',
        'email',
        'bio',
        'para_title',
        'description'
    )

# Register your models here.
admin.site.register(AboutPage, Service)
