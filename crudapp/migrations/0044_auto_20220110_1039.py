# Generated by Django 3.2.10 on 2022-01-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0043_auto_20220108_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220110_10-39-09', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220110_10-39-09', verbose_name='Изображение'),
        ),
    ]
