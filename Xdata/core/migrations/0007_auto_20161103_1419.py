# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20161103_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_conclusao', models.DateField()),
                ('matriz_curricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Matriz_Curricular')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='periodo_conclusao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodo_conclusao', to='core.Periodo'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='periodo_matricula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodo_matricula', to='core.Periodo'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='situacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Situacao'),
        ),
    ]
