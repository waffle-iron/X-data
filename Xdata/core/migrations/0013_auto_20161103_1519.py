# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20161103_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='situacao_aluno',
            old_name='data_registro',
            new_name='data',
        ),
    ]
