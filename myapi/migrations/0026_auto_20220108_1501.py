# Generated by Django 3.2.10 on 2022-01-08 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0025_auto_20220108_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regdevdata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 8, 15, 1, 2, 752828), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regdevdatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 8, 15, 1, 2, 754877), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 8, 15, 1, 2, 752182), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 8, 15, 1, 2, 754153), verbose_name='dt'),
        ),
    ]