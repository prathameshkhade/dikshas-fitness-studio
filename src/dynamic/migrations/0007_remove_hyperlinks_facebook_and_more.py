# Generated by Django 5.0.4 on 2024-04-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0006_hyperlinks_linkdin_hyperlinks_twiter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hyperlinks',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='hyperlinks',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='hyperlinks',
            name='linkdin',
        ),
        migrations.RemoveField(
            model_name='hyperlinks',
            name='twiter',
        ),
        migrations.RemoveField(
            model_name='hyperlinks',
            name='youtube',
        ),
        migrations.AddField(
            model_name='hyperlinks',
            name='link',
            field=models.CharField(default=None, max_length=256, verbose_name='Hyperlink'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hyperlinks',
            name='title',
            field=models.CharField(default=None, max_length=50, verbose_name='Title for hyperlink'),
            preserve_default=False,
        ),
    ]
