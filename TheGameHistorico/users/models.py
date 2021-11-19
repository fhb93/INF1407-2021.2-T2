# from django.db import models
from django.contrib.auth.forms import forms
from django.contrib.auth import models

# Create your models here.
class Usuario(models.User):
    email = forms.EmailField(required=True,
        help_text='email válido', max_length=254)
    
    bio = forms.CharField( 
        required=False,  
        label="Bio",  
        label_suffix=": ",  
        initial=  
            "Espaço para uma breve descrição\nde até 150 caracteres.",
        # help_text="Entre um texto com várias linhas",  
        error_messages = { 
            'required': 'Esse campo área é necessário', 
            'invalid': "Campo área inválido", 
        }, 
        max_length=150, 
        widget=forms.Textarea(attrs={ 
            'class': 'classeArea', 
            'cols': 40, 'rows': 10, 
        }), 
    )
