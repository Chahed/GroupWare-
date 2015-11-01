# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20150423_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Tiitre', models.CharField(max_length=50)),
                ('Appercu', models.TextField()),
                ('Organisateur', models.CharField(max_length=100)),
                ('Duree', models.CharField(max_length=42)),
                ('Pre_requis', models.TextField(max_length=200, null=True)),
                ('Programme', models.TextField(null=True)),
                ('date', models.DateTimeField(verbose_name='Date de parution', null=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Evenement',
        ),
    ]
