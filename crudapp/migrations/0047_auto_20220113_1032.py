# Generated by Django 3.2.10 on 2022-01-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0046_auto_20220112_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='atm',
            name='exDate',
            field=models.DateField(blank=True, null=True, verbose_name='Эксплуатация'),
        ),
        migrations.AddField(
            model_name='atm',
            name='mobile',
            field=models.TextField(blank=True, null=True, verbose_name='Sim'),
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220113_10-32-23', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220113_10-32-23', verbose_name='Изображение'),
        ),
    ]
