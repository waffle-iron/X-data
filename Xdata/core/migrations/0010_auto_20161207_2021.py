# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20161207_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='CEP',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
