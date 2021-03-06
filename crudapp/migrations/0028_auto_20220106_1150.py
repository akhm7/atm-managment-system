# Generated by Django 3.2.10 on 2022-01-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0027_auto_20220106_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220106_11-50-56', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220106_11-50-56', verbose_name='Изображение'),
        ),
    ]
