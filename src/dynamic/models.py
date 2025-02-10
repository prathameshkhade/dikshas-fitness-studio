from django.db import models

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

    class Meta:
        verbose_name_plural = "About Page Information"    

class Archivements(models.Model):
        archivements = models.CharField(("awards and archivements"), max_length=120)

        class Meta:
            verbose_name_plural = "Achivements"

        def __str__(self) -> str:
             return self.archivements.capitalize()

class Hyperlinks(models.Model):
    title = models.CharField(("Title for hyperlink"), max_length=50)
    link = models.URLField(("Hyperlink"), max_length=200)

    class Meta:
        verbose_name_plural = "Hyperlinks"

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
        
class InquiryDetails(models.Model):
     fname = models.CharField(("fname"), max_length=50)
     lname = models.CharField(("lname"), max_length=50)
     email = models.EmailField(("email"), max_length=254)
     mobile = models.BigIntegerField(("mobile"))
     description = models.TextField(("description"))

     class Meta:
         verbose_name_plural = "Inquiry Details"

     def __str__(self) -> str:
          return f"{self.fname.capitalize()} {self.lname.capitalize()}"
     
class Gallery(models.Model):
     gallery_image = models.ImageField(("Gallery Image"), upload_to='gallery/', max_length=100, null=False)

     class Meta:
         verbose_name_plural = "Gallery Image's"

     def __str__(self) -> str:
          return self.gallery_image.url.strip("/")
