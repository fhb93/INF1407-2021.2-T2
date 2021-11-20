'''
Created on Nov 19, 2021

@author: felipe
'''
from sys import executable
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.fields import reverse_related
from django.forms import fields
from django.forms.forms import Form
from django.http import request
# from TheGameHistorico.models import Game

# from TheGameHistorico.settings import TIME_INPUT_FORMATS
   
# formulario de cadastro
class NewUser(UserCreationForm):
    Email = forms.EmailField(required=True, max_length=256)
    # roll_number = forms.IntegerField(
    #                  help_text = "Enter 6 digit roll number"
    #                  )
    Bio = forms.CharField( 
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
