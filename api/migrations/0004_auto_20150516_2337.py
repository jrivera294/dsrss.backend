# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_sources_rss_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sources',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
