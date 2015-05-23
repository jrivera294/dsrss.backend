# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150517_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sources',
            name='category',
            field=models.ForeignKey(to='api.Categories', related_name='sources'),
        ),
    ]
