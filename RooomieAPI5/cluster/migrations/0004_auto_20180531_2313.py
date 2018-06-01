# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-31 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0003_auto_20180530_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meminfo',
            name='EMAIL',
            field=models.EmailField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='meminfo',
            name='GENDER',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='meminfo',
            name='MAJOR',
            field=models.CharField(default='통계학과', max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='meminfo',
            name='NAME',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='meminfo',
            name='PHONE',
            field=models.CharField(max_length=11, null=True),
        ),
    ]