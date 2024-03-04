from django.apps import AppConfig


class ControleContasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.financial_control'
    verbose_name = 'Controle Financeiro de Contas'

    def ready(self) -> None:
        from . import signals  # noqa: F401
