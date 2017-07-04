# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 06:45
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20170702_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyactivity',
            name='base_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dailyactivity',
            name='timestamp',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='dailyactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='timezone',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
