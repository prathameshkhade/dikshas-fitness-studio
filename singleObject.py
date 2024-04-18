from django.db import models

class MySingletonModel(models.Model):
    # Add your model fields here
    field1 = models.CharField(max_length=255)
    field2 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Singleton Object"

    def save(self, *args, **kwargs):
        if self.pk is None:
            # Check if object already exists
            existing_instance = MySingletonModel.objects.filter().exists()
            if existing_instance:
                raise ValidationError("Only one instance of this model is allowed.")
            else:
                super().save(*args, **kwargs)  # Save the first object
        else:
            # Allow updates to the existing object
            super().save(*args, **kwargs)

