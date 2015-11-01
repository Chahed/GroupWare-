# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cours'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cours',
            new_name='doc',
        ),
    ]
