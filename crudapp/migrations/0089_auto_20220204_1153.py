# Generated by Django 3.2.10 on 2022-02-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0088_auto_20220204_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220204_11-52-59', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220204_11-52-59', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='servicecontract',
            name='dataBegin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='servicecontract',
            name='dataEnd',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата конца'),
        ),
        migrations.AlterField(
            model_name='servicecontract',
            name='type',
            field=models.IntegerField(choices=[(0, 'Гарантийное'), (1, 'Сервисное'), (2, 'Отсуствует')], default=0, verbose_name='Вид'),
        ),
    ]
