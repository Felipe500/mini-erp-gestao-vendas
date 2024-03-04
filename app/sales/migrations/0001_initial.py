# Generated by Django 4.2.7 on 2023-11-20 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customers", "0001_initial"),
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    model_utils.fields.AutoCreatedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Criado em",
                    ),
                ),
                (
                    "updated_at",
                    model_utils.fields.AutoLastModifiedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Modificado em",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=7, verbose_name="valor"
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="desconto",
                    ),
                ),
                (
                    "total_discount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="valor total em desconto",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("not_pay", "Aguardando Pagamento"),
                            ("paid", "Pago"),
                            ("cancel", "Cancelado"),
                        ],
                        default="not_pay",
                        max_length=7,
                        verbose_name="status",
                    ),
                ),
                (
                    "is_canceled",
                    models.BooleanField(default=False, verbose_name="venda cancelada"),
                ),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customers.customer",
                        verbose_name="cliente",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="vendendor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Venda",
                "verbose_name_plural": "Vendas",
                "ordering": ["-created_at"],
            },
            managers=[
                ("statistic", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ItemsSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    model_utils.fields.AutoCreatedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Criado em",
                    ),
                ),
                (
                    "updated_at",
                    model_utils.fields.AutoLastModifiedField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Modificado em",
                    ),
                ),
                ("quantity", models.IntegerField(verbose_name="quantidade")),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="desconto"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="produto",
                    ),
                ),
                (
                    "sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sales.sale",
                        verbose_name="Venda",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Itens do pedido",
                "unique_together": {("sale", "product")},
            },
        ),
    ]
