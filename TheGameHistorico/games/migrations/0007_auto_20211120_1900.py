# Generated by Django 3.2.6 on 2021-11-20 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_game_owner_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='title',
            new_name='Título',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='developer',
            new_name='Desenvolvedor',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='publisher',
            new_name='Publicador',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='time_playing',
            new_name='Tempo_de_jogo',
        ),
    ]
