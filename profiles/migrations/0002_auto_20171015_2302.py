# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='display_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.AlterField(
            model_name='profile',
            name='major_of_studies',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='primary_language',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, upload_to='uploads/resume'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secondary_language',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_of_admission',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_of_graduation',
            field=models.DateField(blank=True),
        ),
    ]
