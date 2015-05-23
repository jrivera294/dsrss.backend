# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_categories_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='user_clicks',
            field=models.ManyToManyField(related_name='user_clicks', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
