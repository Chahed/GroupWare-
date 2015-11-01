# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150419_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('titre', models.CharField(null=True, max_length=100)),
                ('auteur', models.CharField(null=True, max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('docfile', models.FileField(upload_to='media/documents', blank=True)),
                ('date', models.DateTimeField(verbose_name='Date de parution', null=True, auto_now_add=True)),
                ('category', models.CharField(null=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='doc',
            name='auteur',
            field=models.CharField(null=True, max_length=42),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc',
            name='category',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc',
            name='date',
            field=models.DateTimeField(verbose_name='Date de parution', null=True, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc',
            name='docfile',
            field=models.FileField(upload_to='media/documents', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doc',
            name='titre',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
    ]
