# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-03 21:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0098_auto_20201204_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 4, 0, 43, 4, 130016), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 4, 0, 43, 4, 131016), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 4, 0, 43, 4, 131016), verbose_name='Дата'),
        ),
    ]
