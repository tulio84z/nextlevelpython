# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 00:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 0, 15, 20, 342186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 0, 15, 20, 341654, tzinfo=utc)),
        ),
    ]