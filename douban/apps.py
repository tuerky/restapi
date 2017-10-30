#douban/apps.py
from django.apps import AppConfig
from suit.apps import DjangoSuitConfig #美化

class CreateapiConfig(AppConfig):
    name = 'douban'

class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'

