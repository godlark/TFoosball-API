# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfoosball', '0005_auto_20161023_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='lost',
            new_name='defence',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='won',
            new_name='offence',
        ),
    ]
