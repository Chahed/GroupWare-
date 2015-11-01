# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150414_2222'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ressource',
        ),
        migrations.AlterField(
            model_name='doc',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
