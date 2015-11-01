# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_auto_20150416_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('confirmation', models.BooleanField(default=False)),
                ('Nom', models.CharField(max_length=120)),
                ('Prenom', models.CharField(max_length=120)),
                ('groupe', models.CharField(choices=[('enseignant', 'enseignant'), ('apprenant', 'apprenant')], default='enseignant', max_length=128, blank=True)),
                ('adresse', models.CharField(max_length=128)),
                ('Tel', models.DecimalField(max_digits=12, decimal_places=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
