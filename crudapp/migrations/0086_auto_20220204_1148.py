# Generated by Django 3.2.10 on 2022-02-04 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0085_auto_20220204_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220204_11-48-31', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220204_11-48-31', verbose_name='Изображение'),
        ),
    ]