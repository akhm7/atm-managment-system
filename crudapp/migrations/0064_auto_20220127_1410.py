# Generated by Django 3.2.10 on 2022-01-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0063_auto_20220127_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220127_14-10-34', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220127_14-10-34', verbose_name='Изображение'),
        ),
    ]
