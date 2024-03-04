from django.utils.translation import gettext_lazy as _
from django.db import models
from app.common.models import Base
from .managers import ProdutoManager, EstoqueManager, CategoriaManager


class Category(Base):
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(verbose_name=_('Ativo?'), default=True)

    objects = CategoriaManager()

    def __str__(self):
        return self.name


class Product(Base):
    description = models.CharField(max_length=100, verbose_name=_('Descrição'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Preço'))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name=_('Categoria'), null=True)
    is_active = models.BooleanField(verbose_name=_('Ativo?'), default=True)

    objects = ProdutoManager()

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.description


class Stock(Base):
    product = models.ForeignKey(Product, verbose_name=_('Produto'), null=True, blank=True, on_delete=models.CASCADE)
    current_stock = models.IntegerField(default=0, verbose_name=_('Estoque atual'))
    minimum_stock = models.IntegerField(default=0, verbose_name=_('Estoque minimo'))
    in_operation = models.IntegerField(default=0, verbose_name=_('Estoque em Operação'))
    is_active = models.BooleanField(verbose_name=_('Ativo?'), default=True)

    objects = EstoqueManager()

    def __str__(self):
        return str(self.product.__str__())

    @staticmethod
    def alter_stock(produto, qted):
        stock_product = Stock.objects.get(product_id=produto)
        stock_product.current_stock += qted
        stock_product.save()

