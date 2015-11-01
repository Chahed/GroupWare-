# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150417_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Tel',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
