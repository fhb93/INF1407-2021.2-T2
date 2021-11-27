# Generated by Django 3.2.6 on 2021-11-27 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=512)),
                ('developer', models.CharField(max_length=512)),
                ('publisher', models.CharField(max_length=512)),
                ('time_playing', models.TimeField(default='00:00:00', null=True)),
                ('status', models.CharField(choices=[('opt1', 'Ainda jogando'), ('opt2', 'Apenas Quest Principal'), ('opt3', 'Principal + alguns Extras'), ('opt4', 'Complecionista')], default='opt1', max_length=100, null=True)),
                ('time_completion', models.DateField(default=django.utils.timezone.now, null=True)),
                ('cover_path', models.CharField(max_length=254, null=True)),
                ('platform', models.CharField(choices=[('opt0', 'Unlisted'), ('opt1', 'Switch'), ('opt2', 'Wii U'), ('opt3', 'Wii'), ('opt4', 'GameCube'), ('opt5', 'N64'), ('opt6', 'SNES'), ('opt7', 'NES'), ('opt8', 'GBA'), ('opt9', 'GBC'), ('opt10', 'GB'), ('opt11', 'PS1'), ('opt12', 'PS2'), ('opt13', 'PS3'), ('opt14', 'PS4'), ('opt15', 'PS5'), ('opt16', 'Xbox'), ('opt17', 'Xbox 360'), ('opt18', 'Xbox One'), ('opt19', 'Xbox Series'), ('opt20', 'PSP'), ('opt21', 'PSVita'), ('opt22', 'NDS'), ('opt23', '3DS'), ('opt24', 'New3DS'), ('opt25', 'Atari 2600'), ('opt26', 'Apple ]['), ('opt27', 'PC')], default='opt0', max_length=15, null=True)),
                ('owner', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
