# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-03 22:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0114_auto_20201204_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 4, 1, 50, 29, 370187), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 4, 1, 50, 29, 371187), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 4, 1, 50, 29, 371187), verbose_name='Дата'),
        ),
    ]