# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-02 16:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201202_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 2, 19, 14, 55, 705527), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 2, 19, 14, 55, 706527), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 2, 19, 14, 55, 706527), verbose_name='Дата'),
        ),
    ]