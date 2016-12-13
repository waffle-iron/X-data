# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20161213_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escola_Origem_Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa')),
                ('tipo_escola_origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_Escola_Origem')),
            ],
        ),
    ]
