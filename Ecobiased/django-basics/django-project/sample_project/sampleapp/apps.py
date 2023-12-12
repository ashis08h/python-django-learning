from django.apps import AppConfig


class SampleappConfig(AppConfig):
    name = 'sampleapp'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import Sampleapp.signals
