from django.apps import AppConfig


class DynamicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.dynamic'
    verbose_name = "Trainer's Personal Details"
