# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_tache'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='text',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
    ]
