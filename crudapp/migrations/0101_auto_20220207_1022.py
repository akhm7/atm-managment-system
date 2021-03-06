# Generated by Django 3.2.10 on 2022-02-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0100_auto_20220207_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220207_10-22-02', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220207_10-22-02', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile_images/default_image_aloqabank.png', upload_to='profile_images/%Y/%m/%d'),
        ),
    ]
