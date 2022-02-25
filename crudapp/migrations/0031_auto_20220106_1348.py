# Generated by Django 3.2.10 on 2022-01-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0030_auto_20220106_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220106_13-48-53', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220106_13-48-53', verbose_name='Изображение'),
        ),
    ]