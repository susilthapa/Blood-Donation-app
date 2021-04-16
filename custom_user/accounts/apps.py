from django.apps import AppConfig
from .signals

class AccountsConfig(AppConfig):
    name = 'accounts'

    # def ready(self):
    #     import accounts.signals
