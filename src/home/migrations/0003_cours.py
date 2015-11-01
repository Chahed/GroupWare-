# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='cours',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
