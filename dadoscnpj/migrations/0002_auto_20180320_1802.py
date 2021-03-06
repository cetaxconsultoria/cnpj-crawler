# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dadoscnpj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=200)),
                ('razao_social', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('situacao', models.CharField(max_length=200)),
                ('natureza_juridica', models.CharField(max_length=200)),
                ('capital_social', models.CharField(max_length=200)),
                ('atividade', models.CharField(max_length=200)),
                ('atividade_sec', models.CharField(max_length=200)),
                ('atividade_sec_1', models.CharField(max_length=200)),
                ('atividade_sec_2', models.CharField(max_length=200)),
                ('atividade_sec_3', models.CharField(max_length=200)),
                ('atividade_sec_4', models.CharField(max_length=200)),
                ('atividade_sec_5', models.CharField(max_length=200)),
                ('atividade_sec_6', models.CharField(max_length=200)),
                ('atividade_sec_7', models.CharField(max_length=200)),
                ('atividade_sec_8', models.CharField(max_length=200)),
                ('atividade_sec_9', models.CharField(max_length=200)),
                ('cep', models.CharField(max_length=200)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('uf', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('socio', models.CharField(max_length=200)),
                ('socio_1', models.CharField(max_length=200)),
                ('socio_2', models.CharField(max_length=200)),
                ('socio_3', models.CharField(max_length=200)),
                ('socio_4', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='AtividadePrincipal',
        ),
        migrations.DeleteModel(
            name='AtividadesSecundarias',
        ),
        migrations.DeleteModel(
            name='Contatos',
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.DeleteModel(
            name='Header',
        ),
        migrations.DeleteModel(
            name='Socios',
        ),
    ]
