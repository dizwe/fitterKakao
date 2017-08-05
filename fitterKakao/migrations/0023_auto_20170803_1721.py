# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-03 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('fitterKakao', '0022_auto_20170731_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='SameClothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_photo', django_resized.forms.ResizedImageField(blank=True, upload_to='top/%Y/%m/%d')),
                ('bot_photo', django_resized.forms.ResizedImageField(blank=True, upload_to='bot/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='ClothesNick',
        ),
    ]