# Generated by Django 3.2.10 on 2022-01-06 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0014_auto_20220106_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regdevdata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 50, 56, 50547), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regdevdatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 50, 56, 52402), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 50, 56, 49766), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 11, 50, 56, 51759), verbose_name='dt'),
        ),
    ]
