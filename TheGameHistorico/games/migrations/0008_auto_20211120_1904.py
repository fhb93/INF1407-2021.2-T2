# Generated by Django 3.2.6 on 2021-11-20 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20211120_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='Desenvolvedor',
            new_name='developer',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='Publicador',
            new_name='publisher',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='Tempo_de_jogo',
            new_name='time_playing',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='Título',
            new_name='title',
        ),
    ]
