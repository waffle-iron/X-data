# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20161103_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Cor'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Sexo'),
        ),
    ]
