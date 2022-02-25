# Generated by Django 3.2.9 on 2021-12-06 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('serialNumber', models.IntegerField(verbose_name='Серийный номер')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('terminalId', models.CharField(blank=True, max_length=255, null=True, verbose_name='Terminal ID')),
            ],
        ),
        migrations.CreateModel(
            name='AtmModelFunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('html', models.TextField(blank=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='brokenCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MfoStruct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='createdAt')),
                ('closed', models.DateTimeField(auto_now_add=True, verbose_name='closed')),
                ('status', models.BooleanField(verbose_name='status')),
                ('broken', models.ManyToManyField(to='crudapp.brokenCategory', verbose_name='Проблема')),
            ],
        ),
        migrations.CreateModel(
            name='telegramMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('chat', models.IntegerField(default=0)),
                ('mid', models.IntegerField(default=0)),
                ('uid', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('ticketId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='crudapp.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='AtmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('company', models.CharField(blank=True, max_length=255, null=True, verbose_name='Компания')),
                ('image', models.ImageField(blank=True, null=True, upload_to='model/model_img_20211206_12-24-24', verbose_name='Изображение')),
                ('functions', models.ManyToManyField(blank=True, to='crudapp.AtmModelFunction', verbose_name='Функционал')),
            ],
        ),
        migrations.CreateModel(
            name='AtmImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='atm_img_20211206_12-24-24', max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='atms/%Y/%m/%d/')),
                ('uploadedAt', models.DateTimeField(auto_now_add=True, verbose_name='uploadedAt')),
                ('atmId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atms', to='crudapp.atm')),
            ],
        ),
        migrations.AddField(
            model_name='atm',
            name='atmModelId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.atmmodel', verbose_name='Модель банкомата'),
        ),
        migrations.AddField(
            model_name='atm',
            name='mfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.mfostruct'),
        ),
    ]