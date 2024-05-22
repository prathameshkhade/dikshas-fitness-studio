from django.db import models
from vercel_storage import blob

# Create your models here.
class AboutPage(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(("image"), upload_to=None, default=None, max_length=150)
    title = models.CharField(max_length=50)
    experience = models.IntegerField()
    email = models.EmailField(max_length=254)
    bio = models.TextField(default="Tell about yourself here...")
    paragraph_title  = models.CharField(max_length=50, default="Enter title here...")
    paragraph_description = models.TextField(default="Describe about your title mentioned above...")

    def save(self, *args, **kwargs):
          if self.img:
               image_file = self.img.file.read()
               vercel_blob_url = blob.put(pathname=f"media/about/{self.img.name}", body=image_file, options={"no_suffix": True})["url"]
               self.img = vercel_blob_url
          super().save(*args, **kwargs)     

class Achivement(models.Model):
        archivements = models.CharField(("awards and archivements"), max_length=120)

        def __str__(self) -> str:
             return self.archivements.capitalize()

class Hyperlink(models.Model):
    title = models.CharField(("Title for hyperlink"), max_length=50)
    link = models.URLField(("Hyperlink"), max_length=200)

    def __str__(self) -> str:
         return f"{self.title}"

    def getdata(self) -> dict:
        try:
            tabledData = Hyperlinks.objects.all()
            data = {}
            for x in tabledData:
                data[x.title] = x.link

        except Exception as e:
             print(e)

        else:
             return data
        
class InquiryDetail(models.Model):
     fname = models.CharField(("fname"), max_length=50)
     lname = models.CharField(("lname"), max_length=50)
     email = models.EmailField(("email"), max_length=254)
     mobile = models.BigIntegerField(("mobile"))
     description = models.TextField(("description"))

     def __str__(self) -> str:
          return f"{self.fname.capitalize()} {self.lname.capitalize()}"
     
class Gallery(models.Model):
     gallery_image = models.ImageField(("Gallery Image"), upload_to=None, max_length=100, null=False)

     def __str__(self) -> str:
          return self.gallery_image.url.strip("/")
     
     def save(self, *args, **kwargs):
          if self.gallery_image:
               image_file = self.gallery_image.file.read()
               vercel_blob_url = blob.put(pathname=f"media/gallery/{self.gallery_image.name}", body=image_file, options={"no_suffix": True})["url"]
               self.gallery_image = vercel_blob_url
          super().save(*args, **kwargs)

     def __del__(self) -> None:
          blob.delete(pathname=f"media/gallery/{self.gallery_image}")
