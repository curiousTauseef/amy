# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0095_add_training_request_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingrequest',
            name='teaching_frequency_expectation',
            field=models.CharField(choices=[('not-at-all', 'Not at all'), ('yearly', 'Once a year'), ('monthly', 'Several times a year'), ('often', 'Primary occupation'), ('other', 'Other (enter below)')], default='not-at-all', max_length=40, verbose_name='How often would you expect to teach classes on Software or Data Carpentry Workshops after this training?'),
        ),
    ]
