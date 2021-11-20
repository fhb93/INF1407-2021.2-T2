# from django.db import models
from django.contrib.auth.forms import forms, UsernameField
from django.contrib.auth import models

# Create your models here.
class Usuario(models.User):
    username = models.User.username
    password = models.User.password
    
    nickname = username
    nickname.primary_key = True
    email = forms.EmailField(required=True,
        help_text='email válido', max_length=254)

    bio = forms.CharField( 
        required=False,  
        label="Bio",  
        label_suffix=": ",  
        initial=  
            "Espaço para uma breve descrição\nde até 150 caracteres.",
        # help_text="Entre um texto com várias linhas",
        max_length=150, 
        widget=forms.Textarea(attrs={ 
            'class': 'classeArea', 
            'cols': 40, 'rows': 10, 
        }), 
    )
