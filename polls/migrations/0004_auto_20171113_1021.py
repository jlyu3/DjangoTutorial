# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20171109_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='frame_folder'),
        ),
    ]
