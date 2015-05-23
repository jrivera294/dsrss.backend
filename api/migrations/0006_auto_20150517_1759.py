# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_categories_subscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sources',
            old_name='categories_id',
            new_name='category',
        ),
    ]
