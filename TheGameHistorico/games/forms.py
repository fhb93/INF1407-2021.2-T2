'''
Created on Nov 20, 2021

@author: felipe
'''
from django import forms

import games
# from . import 


# formulario de cadastro de novo jogo
class NewGameForm(forms.ModelForm):
    class Meta:
        model=games.models.Game
        fields = '__all__'

    # Titulo_do_jogo = forms.CharField(required=True)
    # Desenvolvedor = forms.CharField(required=False)
    # Publicador = forms.CharField(required=False)
    # # Tempo_de_jogo = forms.TimeField(input_formats='%H:%M:%S')
    # Tempo_de_jogo = forms.TimeField(
    #     required=True,  
    #     label="Tempo de jogo",  
    #     label_suffix=": ",  
    #     initial="00:00:00",
    #     show_hidden_initial=True, 
    #     # help_text="Digite um tempo total",  
    #     error_messages = { 
    #     'required': 'Campo necessário', 
    #     'invalid': "Campo de tempo inválido", 
    #     }, 
    #     disabled=False, 
    #     widget=forms.TextInput()
    # )
    #
    # Completou_jogo = forms.ChoiceField( 
    # required=True,  
    # label="O que completou?", 
    # # help_text="Escolha uma opção",  
    # error_messages = { 
    #     'required': 'Campo necessário', 
    #     'invalid': "Campo select inválido", 
    # }, 
    # choices=[ 
    #     ('opt1','Ainda jogando'),
    #     ('opt2','Apenas Quest Principal'),
    #     ('opt3','Principal + alguns Extras'), 
    #     ('opt4','Complecionista'),
    # ], 
    # widget=forms.Select(attrs={ 
    #     'class': 'classeSelect' 
    # }), 
    # ) 