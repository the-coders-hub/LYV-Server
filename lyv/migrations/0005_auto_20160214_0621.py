# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyv', '0004_auto_20160213_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Kannada', 'Kannada'), ('Telugu', 'Telugu'), ('Marathi', 'Marathi'), ('Bengali', 'Bengali'), ('Punjabi', 'Punjabi'), ('English', 'English'), ('Tamil', 'Tamil'), ('Hindi', 'Hindi')], max_length=64),
        ),
    ]
