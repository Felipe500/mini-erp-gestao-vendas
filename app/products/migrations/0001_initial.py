# Generated by Django 3.2.9 on 2023-11-20 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='Categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('current_stock', models.IntegerField(default=0, verbose_name='Estoque atual')),
                ('minimum_stock', models.IntegerField(default=0, verbose_name='Estoque minimo')),
                ('in_operation', models.IntegerField(default=0, verbose_name='Estoque em Operação')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Produto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
