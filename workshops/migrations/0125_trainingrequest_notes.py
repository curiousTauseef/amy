# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-21 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0124_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingrequest',
            name='notes',
            field=models.TextField(blank=True, help_text='Admin notes'),
        ),
    ]