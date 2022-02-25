# Generated by Django 3.2.10 on 2022-02-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0095_auto_20220204_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220204_12-42-11', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220204_12-42-11', verbose_name='Изображение'),
        ),
    ]
