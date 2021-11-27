# from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Bio(models.Model):
    bio_id = models.AutoField(primary_key=True, default=None, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    content= models.TextField(max_length=150)
    def __str__(self):
        return self.title

class Review(models.Model):
    review_id = models.AutoField(primary_key=True, default=None, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    title= models.CharField(max_length=3000)
    content= models.TextField(max_length=150)
    def __str__(self):
        return self.title

    
# # Create your models here.
# class Usuario(User):
#     first_name = None
#     last_name = None
#     is_staff = False
#     is_active = True
#     date_joined = models.DateTimeField(('date joined'), default=now, editable=False)
#     # usuario_id = models.AutoField(default=1, unique=True, primary_key=True)
#
#     username = models.CharField(max_length=64, default='', unique=True, primary_key=True)
#     password1 = models.CharField(('Senha'), max_length=128, default='')
#     password2 = models.CharField(('Confirmar senha'), max_length=128, default='')
#     email = models.CharField(('email'), max_length=254, default='')
#     # nickname = username
#     # nickname.primary_key = True
#     # email = models.EmailField(null=None, max_length=254)
#
#     bio = models.CharField(max_length=150, default=1, blank=True)
#
#
#     # USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = [ 'password1', 'password2' ,'email', ]