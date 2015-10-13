# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gb', '0002_auto_20150929_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='urlname',
            field=models.CharField(default='url1', max_length=100),
            preserve_default=False,
        ),
    ]
