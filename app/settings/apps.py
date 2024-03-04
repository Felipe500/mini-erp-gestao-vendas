from django.apps import AppConfig


class ConfiguracoesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.settings'

    verbose_name = 'Configurações'