# Generated by Django 3.2.10 on 2021-12-29 05:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regdevdata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 4, 37, 5999), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regdevdatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 4, 37, 7887), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 4, 37, 5275), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 4, 37, 7256), verbose_name='dt'),
        ),
    ]
