# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyv', '0005_auto_20160214_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Marathi', 'Marathi'), ('Telugu', 'Telugu'), ('Kannada', 'Kannada'), ('Bengali', 'Bengali'), ('Tamil', 'Tamil'), ('Hindi', 'Hindi'), ('English', 'English'), ('Punjabi', 'Punjabi')], max_length=64),
        ),
    ]
