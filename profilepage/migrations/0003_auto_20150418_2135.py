# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0002_auto_20150416_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='username',
            field=models.CharField(default=b'pre-database', max_length=20),
        ),
        migrations.AlterField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
