from django.apps import AppConfig


class ElasticConfig(AppConfig):
    name = 'elastic'

    def ready(self):
        import elastic.signals
