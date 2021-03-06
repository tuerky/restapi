# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=20)),
                ('score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('starring', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='moovie',
        ),
    ]
