# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150417_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Tel',
            field=models.DecimalField(decimal_places=0, max_digits=12),
            preserve_default=True,
        ),
    ]
