# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-25 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.FileField(blank=True, default='static/abc1.jpg', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, default='abc.jpg', upload_to=b''),
            preserve_default=False,
        ),
    ]
