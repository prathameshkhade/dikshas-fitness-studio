from django.db import models

# Create your models here.
class ClassInfo(models.Model):
    # class_img = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    class_title = models.CharField(("class title"), max_length=50) 
    class_week = models.CharField(("enter week"), max_length=50) 
    class_time = models.CharField(("enter time"), max_length=50) 
    class_description = models.TextField(("enter description"))

    def __str__(self) -> str:
        return f"{self.class_title}"
    
    def getdata(self) -> dict:
        try:
            table_data = ClassInfo.objects.all()

            data = {}
            for obj in table_data:
                data[obj] = {
                    'title': obj.class_title,
                    'week': obj.class_week,
                    'time': obj.class_time,
                    'description': obj.class_description
                }

        except Exception as e:
            print(e)

        else:
            return data

