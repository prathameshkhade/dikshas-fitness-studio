from django.db import models
from tinymce.models import HTMLField
from src.utils import generate_slug

class Events(models.Model):
    class Meta:
        verbose_name_plural = "Events"

    title = models.CharField(("Event title"), max_length=50)
    date = models.DateTimeField(("Date and Time of the event"), auto_now=False, auto_now_add=False)
    image = models.ImageField(("Image"), upload_to=None, max_length=150, default="staticfiles/static/img/classes/3.jpg")
    time = models.PositiveIntegerField(("Total event time (duration in minutes):"), default=60)
    description = HTMLField()
    slug = models.SlugField(unique=True, null=True, default=None)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(string=self.title, model=Events)
        super().save(*args, **kwargs)
