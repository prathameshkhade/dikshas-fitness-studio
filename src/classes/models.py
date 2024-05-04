from django.db import models
from vercel_storage import blob

# Create your models here.
class ClassInfo(models.Model):
    class_img = models.ImageField(("image"), upload_to=None, max_length=150, default="staticfiles/static/img/classes/3.jpg")
    class_title = models.CharField(("class title"), max_length=50) 
    class_week = models.CharField(("enter week"), max_length=50) 
    class_time = models.CharField(("enter time"), max_length=50) 
    class_description = models.TextField(("enter description"))

    def __str__(self) -> str:
        return f"{self.class_title}"
    
    def save(self, *args, **kwargs):
        if self.class_img:
            # Read the image file
            image_file = self.class_img.file.read()

            # Upload the image file to Vercel Blob
            # Replace 'YOUR_VERCEL_BLOB_UPLOAD_CODE' with your actual code to upload the file to Vercel Blob
            vercel_blob_url = blob.put(pathname=f"media/classes/{self.class_img.name}", body=image_file, options={"no_suffix": True})["url"]

            # Save the Vercel Blob URL in the imageField
            self.class_img = vercel_blob_url

        super().save(*args, **kwargs)

    def getdata(self) -> dict:
        try:
            table_data = ClassInfo.objects.all()

            data = {}
            i = 1
            for obj in table_data:
                data[i] = {
                    'img': obj.class_img,
                    'title': obj.class_title,
                    'week': obj.class_week,
                    'time': obj.class_time,
                    'description': obj.class_description
                }
                i += 1

        except Exception as e:
            print(e)

        else:
            return data
    
    def __del__(self):
        blob.delete(self.class_img)

