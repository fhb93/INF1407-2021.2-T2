# Generated by Django 3.2.6 on 2021-11-27 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='time_playing',
            field=models.TimeField(default='00:00:00', null=True),
        ),
    ]
