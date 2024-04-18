from django.db import models

# Create your models here.
class AboutPage(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    experience = models.IntegerField()
    email = models.EmailField(max_length=254)
    bio = models.TextField()
    para_title  = models.CharField(max_length=50)
    description = models.TextField()
