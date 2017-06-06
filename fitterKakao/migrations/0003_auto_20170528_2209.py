# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-28 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitterKakao', '0002_auto_20170527_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='chest_a',
            field=models.IntegerField(choices=[(0, '많이 남는다'), (1, '별로 불편한 것이 없다'), (2, '낀다')], default=1),
        ),
        migrations.AddField(
            model_name='person',
            name='sleeve_a',
            field=models.IntegerField(choices=[(0, '많이 남는다'), (1, '별로 불편한 것이 없다'), (2, '낀다')], default=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='shoulder_a',
            field=models.IntegerField(choices=[(0, '많이 남는다'), (1, '별로 불편한 것이 없다'), (2, '낀다')], default=1),
        ),
    ]
