'''
Created on Nov 19, 2021

@author: felipe
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm

import users
from users.models import Bio


# from django.contrib.auth.models import User
# from TheGameHistorico.models import Game
# from TheGameHistorico.settings import TIME_INPUT_FORMATS
class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = '__all__'
        
    content = forms.CharField( 
        required=False,  
        label="Bio",  
        label_suffix=": ",  
        # help_text="Entre um texto com várias linhas",  
        max_length=150, 
        widget=forms.Textarea(attrs={ 
            'class': 'classeArea', 
            'cols': 40, 'rows': 10,
            'placeholder': "Espaço para uma breve descrição\nde até 150 caracteres." 
        }), 
    )
     
# formulario de cadastro
class NewUserForm(UserCreationForm):

    class Meta:
        model = users.models.User
        fields = ["username", "password1", "password2", "email", ]
        # fields = ["username", "password1", "password2", "email", "bio"] 
    # Note: the last two fields have changed

    # email = forms.EmailField(required=True, max_length=254)
    # roll_number = forms.IntegerField(
    #                  help_text = "Enter 6 digit roll number"
    #                  )
    # senha=forms.CharField(widget=forms.PasswordInput())
    #
    # confirmar_senha=forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(label='Nome de Usuário', widget= forms.TextInput(attrs={'placeholder' : 'Digite um nome de usuário'}))
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))                      
    password2 = forms.CharField(label= 'Confirmar Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha'}))
    email = forms.EmailField(label= 'Endereço de email', widget=forms.EmailInput(attrs={'placeholder': 'Digite seu email'}))
   
    
    
    
    # def save(self):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.bio = self.bio
    #     user.save()
    #     return user
 