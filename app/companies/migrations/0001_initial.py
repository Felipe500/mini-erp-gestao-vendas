# Generated by Django 3.2.9 on 2023-11-20 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Criado em')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('business_name', models.CharField(max_length=100)),
                ('document', models.CharField(blank=True, max_length=130, null=True, verbose_name='CNPJ')),
                ('zipcode', models.CharField(blank=True, max_length=40, null=True, verbose_name='Cep')),
                ('uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cidade')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Endereço')),
                ('complement', models.CharField(blank=True, max_length=250, null=True, verbose_name='Complemento')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_blocked', models.BooleanField(default=False, verbose_name='Bloqueado ?')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
                'db_table': 'companies_company_users',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='users',
            field=models.ManyToManyField(related_name='users_in_company', through='companies.UserCompany', to=settings.AUTH_USER_MODEL),
        ),
    ]
