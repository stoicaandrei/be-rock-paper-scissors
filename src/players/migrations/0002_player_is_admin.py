# Generated by Django 2.2.5 on 2020-09-13 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
