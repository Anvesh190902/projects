# Generated by Django 4.2.7 on 2023-11-18 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_newtable'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewTable',
            new_name='Order',
        ),
    ]
