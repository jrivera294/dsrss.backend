# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20150626_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]
