# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_auto_20150517_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='categories', blank=True),
        ),
    ]
