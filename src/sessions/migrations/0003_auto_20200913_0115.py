# Generated by Django 2.2.5 on 2020-09-13 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0002_session_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]
