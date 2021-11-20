from django.db import models

# Create your models here.


class Game(models.Model):
    BOOL_VALS =((0,'False'), (1, 'True'),)
    id=models.PositiveBigIntegerField()
    id.primary_key = True
    title= models.CharField(max_length=512)
    developer=models.CharField(max_length=512)
    publisher=models.CharField(max_length=512)
    playing=models.IntegerField(choices=BOOL_VALS)
    mainquest=models.IntegerField(choices=BOOL_VALS)
    mainquestPlus=models.IntegerField(choices=BOOL_VALS)
    complete=models.IntegerField(choices=BOOL_VALS)

    # def __str__(self):
    #     return self.title
