from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Petstagram.accounts'

    def ready(self):
        import Petstagram.accounts.signals
