# Generated by Django 2.2.10 on 2020-04-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extrequests', '0018_auto_20200106_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selforganisedsubmission',
            name='workshop_url',
            field=models.URLField(blank=True, default='', help_text='Use the link to the website, not the repository. This is typically in the format <a>https://username.github.io/YYYY-MM-DD-sitename</a>.  If you are running an online workshop, please use the format YYYY-MM-DD-sitename-online.', max_length=255, verbose_name='Please share your workshop URL'),
        ),
    ]
