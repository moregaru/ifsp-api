# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-28 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('prontuario', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
            ],
        ),
    ]
