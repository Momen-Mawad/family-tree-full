# Generated by Django 3.2.5 on 2021-08-01 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family_tree', '0003_familydata_partner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familydata',
            old_name='mother',
            new_name='picture',
        ),
    ]
