# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20141016_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom',
            field=models.CharField(default=b'SOME CATEGORIE', max_length=100),
            preserve_default=True,
        ),
    ]
