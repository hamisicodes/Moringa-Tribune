# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-20 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
