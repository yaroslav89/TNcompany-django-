# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20160102_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
