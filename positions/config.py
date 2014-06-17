from django.apps import AppConfig
from django.utils.importlib import import_module


class PositionsConfig(AppConfig):
    name = 'positions'
    verbose_name = 'Positions'

    def ready(self):
        import_module('positions.collections')
