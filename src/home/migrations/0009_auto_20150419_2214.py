# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150417_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='groupe',
        ),
        migrations.AlterField(
            model_name='doc',
            name='docfile',
            field=models.FileField(upload_to='media/documents/', blank=True),
            preserve_default=True,
        ),
    ]
