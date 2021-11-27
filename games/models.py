from _datetime import date

from django.db import models
import django.utils.timezone

from users.models import User 


# Create your models here.
class Game(models.Model):
    BOOL_VALS =((0,'False'), (1, 'True'),)
    id=models.AutoField(primary_key=True, unique=True, default=None)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name="usuario_username", editable=False)
    # user_username = models.ForeignKey(users.models.Usuario, default=1, verbose_name="Usuario", on_delete=models.SET_DEFAULT)
    title= models.CharField(max_length=512)
    developer=models.CharField(max_length=512)
    publisher=models.CharField(max_length=512)
    # playing=models.IntegerField(choices=BOOL_VALS)
    # mainquest=models.IntegerField(choices=BOOL_VALS)
    # mainquestPlus=models.IntegerField(choices=BOOL_VALS)
    # complete=models.IntegerField(choices=BOOL_VALS)
    time_playing=models.TimeField(default='00:00:00', null=True)
    CHOICES = (
        ('opt1','Ainda jogando'),
        ('opt2','Apenas Quest Principal'),
        ('opt3','Principal + alguns Extras'), 
        ('opt4','Complecionista'),
        )

    
    status=models.CharField(max_length=100, choices = CHOICES, default='opt1')
    
    time_completion = models.DateField(default= django.utils.timezone.now, null=True)
    
    cover_path=models.CharField(max_length=254, null=True)
    PLATS = (
        ('opt0', 'Unlisted'),
        ( 'opt1', 'Switch' ),
        ('opt2', 'Wii U'),
        ('opt3', 'Wii'),
        ('opt4', 'GameCube'),
        ('opt5', 'N64'),
        ('opt6', 'SNES'),
        ('opt7', 'NES'),
        ('opt8' , 'GBA'),
        ('opt9', 'GBC'),
        ('opt10', 'GB'),
        ( 'opt11', 'PS1' ),
        ( 'opt12', 'PS2' ),
        ( 'opt13', 'PS3' ),
        ( 'opt14', 'PS4' ),
        ( 'opt15', 'PS5' ),
        ( 'opt16', 'Xbox' ),
        ( 'opt17', 'Xbox 360' ),
        ('opt18' , 'Xbox One'),
        ('opt19' , 'Xbox Series'),
        ('opt20', 'PSP'),
        ('opt21', 'PSVita'),
        ('opt22', 'NDS' ),
        ('opt23', '3DS'),
        ('opt24', 'New3DS'),
        ('opt25', 'Atari 2600'),
        ('opt26', 'Apple ]['),
        ('opt27' , 'PC'),
        )
    platform = models.CharField(max_length=15, choices = PLATS, default ='opt0')
    # def __str__(self):
    #     return self.title
