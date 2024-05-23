from django.db import models
from datetime import timedelta

# Create your models here.
class User_Management(models.Model):
    Subscription_Option = [
        ('kids', 'Kids'),
        ('adult', 'Adult'),
        ('personal_training', 'Personal Training'),
        ('other', 'Other')
    ]

    Batch_Time_Options = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('weekends', 'Weekends')
    ]

    Blood_Group_Options = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('other', 'Other')
    ]

    Client_Name = models.CharField(max_length=50)

    Subscription_Type = models.CharField(max_length=20,
                        choices=Subscription_Option,)
    
    Subscription_Date_From = models.DateField()
    Subscription_Date_To = models.DateField(auto_now_add=True)

    Mobile_No = models.CharField(max_length=10)
    Address = models.CharField(max_length=200)
    Batch_Time = models.CharField(max_length=20, choices=Batch_Time_Options)
    Blood_Group = models.CharField(max_length=10, choices=Blood_Group_Options)
    Weight = models.FloatField()
    Height = models.FloatField()
    Medical_Issue = models.CharField(max_length=100)
    Taking_Medicine = models.CharField(max_length=100)
    Reason_For_Joining = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Student Information"

    def save(self, *args, **kwargs):
        # Set Subscription_Date_To as Subscription_Date_From + 1 month
        self.Subscription_Date_To = self.Subscription_Date_From + timedelta(days=30)
        super().save(*args, **kwargs)
