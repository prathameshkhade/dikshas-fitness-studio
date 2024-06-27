from django.contrib import admin
from .models import Events

class ServiceEvents(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        "title",
        "date",
        "description"
    )

admin.site.register(Events, ServiceEvents)