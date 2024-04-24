from django.contrib import admin
from .models import User_Management

# Register your models here.
class Service(admin.ModelAdmin):
    list_display = (
        'Client_Name',
        "Subscription_Type",
        "Subscription_Date_From",
        "Subscription_Date_To",
        "Mobile_No",
        "Address",
        "Batch_Time",
        "Blood_Group",
        "Weight",
        "Height",
        "Medical_Issue",
        "Taking_Medicine",
        "Reason_For_Joining",
    )
    list_per_page = 10

admin.site.register(User_Management, Service)
