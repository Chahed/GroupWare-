# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20150423_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
