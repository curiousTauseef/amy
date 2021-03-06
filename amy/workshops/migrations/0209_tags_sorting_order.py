# Generated by Django 2.2.9 on 2020-01-10 11:54

from django.db import migrations


def tags_priority(apps, schema_editor):
    Tag = apps.get_model('workshops', 'Tag')

    tag_order = [
        'DC',
        'LC',
        'SWC',
        'Circuits',
        'Pilot',
        'TTT',
        'online',
        'ITT',
        'cancelled',
        'unresponsive',
        'stalled',
        'LMO',
        'LSO',
        'WiSE',
        'hackathon',
    ]
    for priority, tag in enumerate(tag_order):
        Tag.objects.filter(name=tag).update(priority=priority + 1)


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0208_auto_20200110_1103'),
    ]

    operations = [
        migrations.RunPython(tags_priority),
    ]
