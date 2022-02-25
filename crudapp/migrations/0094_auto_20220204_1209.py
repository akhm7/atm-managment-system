# Generated by Django 3.2.10 on 2022-02-04 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0093_auto_20220204_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.servicecontract', verbose_name='Обслуживание'),
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220204_12-09-54', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220204_12-09-54', verbose_name='Изображение'),
        ),
    ]
