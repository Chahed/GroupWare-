# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20150421_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evenement',
            name='evenement',
        ),
    ]
