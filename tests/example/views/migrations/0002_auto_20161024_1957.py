# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listdata',
            name='select',
            field=models.CharField(choices=[(10, b'10'), (20, b'20'), (30, b'Dertig'), (40, b'40')], default=40, max_length=8),
        ),
        migrations.AlterField(
            model_name='listdata',
            name='boolean',
            field=models.BooleanField(default=True, help_text=b'True or False'),
        ),
        migrations.AlterField(
            model_name='listdata',
            name='name',
            field=models.CharField(help_text=b'Get a unique name', max_length=50),
        ),
    ]