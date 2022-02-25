# Generated by Django 3.2.10 on 2022-01-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0033_auto_20220107_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmimage',
            name='title',
            field=models.CharField(default='atm_img_20220107_18-03-42', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='atmmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model/model_img_20220107_18-03-42', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='telegrammsg',
            name='t',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='crudapp.ticket'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='mfo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.mfostruct'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='atm',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.atm'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='broken',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='crudapp.brokenCategory', verbose_name='Проблема'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.telegramuser'),
        ),
    ]