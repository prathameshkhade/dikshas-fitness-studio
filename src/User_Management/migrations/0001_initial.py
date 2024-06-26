# Generated by Django 5.0.4 on 2024-04-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User_Management",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Client_Name", models.CharField(max_length=50)),
                (
                    "Subscription_Type",
                    models.CharField(
                        choices=[
                            ("Kids", "kids"),
                            ("Adult", "adult"),
                            ("Personal Training", "personal_training"),
                            ("Other", "other"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
