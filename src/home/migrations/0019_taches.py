# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20150428_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taches',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateTimeField(null=True, verbose_name='Date de parution', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
