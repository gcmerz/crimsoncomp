# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contributor',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contributor',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
