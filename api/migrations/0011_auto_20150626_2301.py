# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertising',
            name='user_clicks',
        ),
        migrations.AlterField(
            model_name='advertising',
            name='clicks',
            field=models.BigIntegerField(default=0),
        ),
    ]
