# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dadoscnpj', '0004_cnpj_cnpj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cnpj',
            name='cnpj',
        ),
    ]