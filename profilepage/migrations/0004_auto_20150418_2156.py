# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0003_auto_20150418_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
