from django.db import models

# Create your models here.
class AboutPage(models.Model):
    # image = models.ImageField(upload_to="statc/", height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    experience = models.IntegerField()
    email = models.EmailField(max_length=254)
    bio = models.TextField(default="Tell about yourself here...")
    paragraph_title  = models.CharField(max_length=50, default="Enter title here...")
    paragraph_description = models.TextField(default="Describe about your title mentioned above...")

    class Archivements:
        archivements = models.CharField(max_length=120)

class Hyperlinks(models.Model):
    facebook = models.CharField(("facebook link"), max_length=200)
    instagram = models.CharField(("instagram link"), max_length=200)
    youtube = models.CharField(("youtube link"), max_length=1024)