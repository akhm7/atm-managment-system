# Generated by Django 3.2.10 on 2022-01-06 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_auto_20220105_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regdevdata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 12, 42, 372258), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regdevdatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 12, 42, 374158), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 12, 42, 371388), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 12, 42, 373524), verbose_name='dt'),
        ),
    ]
