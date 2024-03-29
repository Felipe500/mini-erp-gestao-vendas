# Generated by Django 4.2.7 on 2024-01-03 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "financial_control",
            "0003_alter_movements_movement_alter_movements_val_card_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Movement",
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
                    "type",
                    models.CharField(
                        choices=[(0, "saida"), (1, "entrada")],
                        max_length=2,
                        verbose_name="TIPO",
                    ),
                ),
                ("id_object", models.CharField(blank=True, max_length=16, null=True)),
                (
                    "movement",
                    models.CharField(
                        choices=[
                            ("account_paid", "Conta Paga"),
                            ("account_received", "Conta Recebida"),
                            ("sale", "Concluida Venda"),
                            ("expenses", "Despesas"),
                        ],
                        max_length=18,
                    ),
                ),
                ("detail_movement", models.CharField(max_length=35)),
                (
                    "form_pg",
                    models.CharField(
                        choices=[
                            ("1", "ESPECIE"),
                            ("2", "PIX"),
                            ("3", "CARTAO"),
                            ("4", "ESPECIE E PIX"),
                            ("5", "ESPECIE E CARTÃO"),
                            ("6", "PIX E CARTÃO"),
                            ("7", "ESPECIE, PIX E CARTÃO"),
                        ],
                        max_length=50,
                        verbose_name="Forma de pagamento",
                    ),
                ),
                (
                    "val_card",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "val_card_liq",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "val_pix",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "val_money",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "value",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "data_movement",
                    models.JSONField(default=dict, verbose_name="Dados do Movimento"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Vendendor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Movimentação",
                "verbose_name_plural": "Movimentações",
            },
        ),
    ]
