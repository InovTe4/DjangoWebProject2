# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-17 17:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201117_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 17, 20, 55, 7, 629378), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 17, 20, 55, 7, 629378), verbose_name='Дата'),
        ),
    ]
