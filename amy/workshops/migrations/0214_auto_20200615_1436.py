# Generated by Django 2.2.10 on 2020-06-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0213_auto_20200501_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshoprequest',
            name='number_attendees',
            field=models.CharField(choices=[('10-40', '10-40 (one room, two instructors)'), ('40-80', '40-80 (two rooms, four instructors)'), ('80-120', '80-120 (three rooms, six instructors)')], default=None, help_text="These recommendations are for in-person workshops. This number doesn't need to be precise, but will help us decide how many instructors your workshop will need. Each workshop must have at least two instructors.<br>For online Carpentries workshops, we recommend a maximum of 20 learners per class. If your workshop attendance will exceed 20 learners please be sure to include a note in the comments section below. ", max_length=15, verbose_name='Anticipated number of attendees'),
        ),
    ]
