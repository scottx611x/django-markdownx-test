# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 18:27
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_mymodel_markdownx_field3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='markdownx_field2',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='markdownx_field3',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
    ]
