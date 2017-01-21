# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_vendor_mod_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='vendor',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name2',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]