# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0019_auto_20161025_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='enclosure_url',
            field=models.URLField(db_index=True, default=None, max_length=300, unique=True),
        ),
    ]
