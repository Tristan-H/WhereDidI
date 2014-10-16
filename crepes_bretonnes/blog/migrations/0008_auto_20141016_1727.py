# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20141016_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fb',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
