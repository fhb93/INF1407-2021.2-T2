from django import forms
from django.contrib.auth.forms import UserCreationForm
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

# formulario de cadastro de novo jogo
class NewGame(forms.ModelForm):
    # class Meta:
    #     model=Publisher

    Titulo_do_jogo = forms.CharField(required=True)
    Desenvolvedor = forms.CharField(required=False)
    Publicador = forms.CharField(required=False)
    # Tempo_de_jogo = forms.TimeField(input_formats='%H:%M:%S')
    Tempo_de_jogo = forms.TimeField(
        required=True,  
        label="Tempo de jogo",  
        label_suffix=": ",  
        initial="00:00:00",  
        # help_text="Digite um tempo total",  
        error_messages = { 
        'required': 'Campo necessário', 
        'invalid': "Campo de tempo inválido", 
        }, 
        disabled=False, 
        widget=forms.TimeInput(format=TIME_INPUT_FORMATS[0]),
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