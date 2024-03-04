from django.apps import AppConfig


class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.products'

    verbose_name = 'Produtos'

    def ready(self):
        import app.products.signal