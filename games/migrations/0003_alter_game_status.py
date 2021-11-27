# Generated by Django 3.2.6 on 2021-11-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_time_playing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('opt1', 'Ainda jogando'), ('opt2', 'Apenas Quest Principal'), ('opt3', 'Principal + alguns Extras'), ('opt4', 'Complecionista')], default='opt1', max_length=100, null=True),
        ),
    ]
