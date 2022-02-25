# Generated by Django 3.2.10 on 2022-01-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0077_auto_20220131_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='inBankProcessing',
            field=models.IntegerField(choices=[(0, 'Внешний процессинг'), (1, 'Внутренний процессинг')], default=0, verbose_name='Процессинговый центр'),
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220131_16-08-50', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220131_16-08-50', verbose_name='Изображение'),
        ),
    ]