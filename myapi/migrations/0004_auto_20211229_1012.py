# Generated by Django 3.2.10 on 2021-12-29 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20211229_1006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestdata',
            options={'verbose_name': 'File', 'verbose_name_plural': 'Files'},
        ),
        migrations.AlterField(
            model_name='regdevdata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 12, 48, 711231), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regdevdatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 12, 48, 713048), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedata',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 12, 48, 710504), verbose_name='dt'),
        ),
        migrations.AlterField(
            model_name='regtsedatatest',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 29, 10, 12, 48, 712393), verbose_name='dt'),
        ),
    ]