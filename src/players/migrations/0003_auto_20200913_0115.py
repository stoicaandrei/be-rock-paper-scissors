# Generated by Django 2.2.5 on 2020-09-13 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='sessions.Session'),
        ),
    ]
