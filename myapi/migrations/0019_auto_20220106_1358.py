# Generated by Django 3.2.10 on 2022-01-06 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0018_auto_20220106_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regdevdata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 13, 58, 51, 314168), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regdevdatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 13, 58, 51, 316164), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 13, 58, 51, 313528), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 13, 58, 51, 315455), verbose_name='dt'),
        ),
    ]
