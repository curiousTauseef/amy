# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0101_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
