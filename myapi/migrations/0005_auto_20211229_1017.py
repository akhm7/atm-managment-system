# Generated by Django 3.2.10 on 2021-12-29 05:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20211229_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestdatatest',
            name='response',
        ),
        migrations.AlterField(
            model_name='regdevdata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 17, 36, 909414), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regdevdatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 17, 36, 911172), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 17, 36, 908683), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 17, 36, 910564), verbose_name='dt'),
        ),
    ]
