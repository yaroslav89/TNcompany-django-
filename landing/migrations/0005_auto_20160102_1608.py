# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 16:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20160102_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='img_url',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='img_url',
            new_name='img',
        ),
    ]