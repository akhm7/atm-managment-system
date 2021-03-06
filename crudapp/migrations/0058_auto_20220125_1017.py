# Generated by Django 3.2.10 on 2022-01-25 05:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0057_auto_20220118_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramuser',
            options={'verbose_name': 'Сервисдеск Пользователи', 'verbose_name_plural': 'Сервисдеск Пользователи'},
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='image',
            field=models.ImageField(upload_to='atms/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220125_10-17-47', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220125_10-17-47', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='json_info',
            field=models.TextField(blank=True, default='', null=True, verbose_name='JSON'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='mfo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.mfostruct', verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='stage',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Действие'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='status',
            field=models.IntegerField(choices=[(0, 'Неавторизован'), (1, 'Авторизован')], default=0, verbose_name='Авторизация'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='uid',
            field=models.IntegerField(default=0, verbose_name='Telegram User ID'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='atm',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.atm', verbose_name='Банкомат'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dataClosed',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Закрыт'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dataCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='edited',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Редактирование'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='operator',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Модератор'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Открыто'), (1, 'Закрыто'), (2, 'Отменено'), (3, 'Сервисное обслуживание'), (4, 'В работе'), (5, 'Неизвестно')], default=5, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.telegramuser', verbose_name='Пользователь (Telegram)'),
        ),
    ]
