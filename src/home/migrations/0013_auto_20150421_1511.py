# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150420_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Organisateur', models.CharField(max_length=100)),
                ('Duree', models.CharField(max_length=42)),
                ('Pre_requis', models.TextField(null=True)),
                ('Programme', models.TextField(null=True)),
                ('evenement', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='actualite',
            name='image',
            field=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actualite',
            name='url',
            field=models.URLField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='actualite',
            name='titre',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
