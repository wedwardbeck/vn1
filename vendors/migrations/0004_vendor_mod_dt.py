# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20170116_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='mod_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
