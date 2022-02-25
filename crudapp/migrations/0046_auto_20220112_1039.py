# Generated by Django 3.2.10 on 2022-01-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0045_auto_20220110_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='json_info',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220112_10-39-13', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220112_10-39-13', verbose_name='Изображение'),
        ),
    ]