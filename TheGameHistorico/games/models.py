from django.db import models
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
    time_playing=models.TimeField(default='00:00:00')
    CHOICES = (
        ('opt1','Ainda jogando'),
        ('opt2','Apenas Quest Principal'),
        ('opt3','Principal + alguns Extras'), 
        ('opt4','Complecionista'),
        )
    status=models.CharField(max_length=100, choices = CHOICES, default='opt1')
    cover_path=models.CharField(max_length=254, null=True)
    # def __str__(self):
    #     return self.title
