# Generated by Django 5.0.4 on 2024-04-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0007_remove_hyperlinks_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hyperlinks',
            name='link',
            field=models.URLField(verbose_name='Hyperlink'),
        ),
    ]
