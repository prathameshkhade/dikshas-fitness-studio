# Generated by Django 5.0.4 on 2024-04-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0002_remove_aboutpage_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hyperlinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=200, verbose_name='facebook link')),
                ('instagram', models.CharField(max_length=200, verbose_name='instagram link')),
                ('youtube', models.CharField(max_length=1024, verbose_name='youtube link')),
            ],
        ),
    ]