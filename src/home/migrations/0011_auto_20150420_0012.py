# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150419_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='docfile',
            field=models.FileField(upload_to='profile_images/', blank=True),
            preserve_default=True,
        ),
    ]
