from sys import executable
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.fields import reverse_related
from django.forms import fields
from django.forms.forms import Form
from django.http import request

from TheGameHistorico.settings import TIME_INPUT_FORMATS
   
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


# formulario de cadastro de novo jogo
class NewGameForm(forms.ModelForm):
    class Meta:
        model=Game
        fields= []
        

    Titulo_do_jogo = forms.CharField(required=True)
    Desenvolvedor = forms.CharField(required=False)
    Publicador = forms.CharField(required=False)
    # Tempo_de_jogo = forms.TimeField(input_formats='%H:%M:%S')
    Tempo_de_jogo = forms.DurationField(
        required=True,  
        label="Tempo de jogo",  
        label_suffix=": ",  
        initial="00:00:00",
        show_hidden_initial=True, 
        # help_text="Digite um tempo total",  
        error_messages = { 
        'required': 'Campo necessário', 
        'invalid': "Campo de tempo inválido", 
        }, 
        disabled=False, 
        widget=forms.TextInput()
    )

    Completou_jogo = forms.ChoiceField( 
    required=True,  
    label="O que completou?",  
    label_suffix=": ",  
    initial="opt1",  
    # help_text="Escolha uma opção",  
    error_messages = { 
        'required': 'Campo necessário', 
        'invalid': "Campo select inválido", 
    }, 
    choices=[ 
        ('opt1','Ainda jogando'),
        ('opt2','Apenas Quest Principal'),
        ('opt3','Principal + alguns Extras'), 
        ('opt4','Complecionista'),
    ], 
    widget=forms.Select(attrs={ 
        'class': 'classeSelect' 
    }), 
    ) 