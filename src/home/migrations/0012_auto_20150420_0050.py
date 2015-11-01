# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20150420_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='docfile',
            field=models.FileField(upload_to='files/', blank=True),
            preserve_default=True,
        ),
    ]
