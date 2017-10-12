# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsSys', '0004_auto_20170930_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinfo',
            name='p_price',
        ),
        migrations.AddField(
            model_name='productinfo',
            name='p_info',
            field=models.TextField(blank=True, null=True, verbose_name='商品信息'),
        ),
    ]