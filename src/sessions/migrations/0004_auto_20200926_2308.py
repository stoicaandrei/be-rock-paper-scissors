# Generated by Django 2.2.5 on 2020-09-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0003_auto_20200913_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='timer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, 'pending'), (1, 'playing'), (2, 'waiting'), (3, 'finished')], default=0),
        ),
    ]
