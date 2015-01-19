# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.PositiveSmallIntegerField(choices=[(0, b'proposal'), (1, b'wish'), (2, b'participate')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
