# Generated by Django 3.2.10 on 2021-12-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0015_auto_20211224_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20211224_14-13-52', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20211224_14-13-52', verbose_name='Изображение'),
        ),
    ]