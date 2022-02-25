# Generated by Django 3.2.10 on 2022-01-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0051_auto_20220117_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pcipts',
            options={'verbose_name': 'PCIPTS', 'verbose_name_plural': 'PCIPTS'},
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220117_11-50-59', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220117_11-50-59', verbose_name='Изображение'),
        ),
    ]
