# Generated by Django 3.2.10 on 2022-02-04 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0081_auto_20220201_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='atm',
            name='service',
            field=models.IntegerField(choices=[(0, 'Отсуствует'), (1, 'Сервисное'), (2, 'Гарантийное')], default=0, verbose_name='Обслуживание'),
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220204_10-30-38', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220204_10-30-38', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default_image_aloqabank.png', upload_to='profile_images')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.telegramuser')),
            ],
        ),
    ]
