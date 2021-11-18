from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.forms import Form
   
# formulario de cadastro
class NewUser(UserCreationForm):
    Email = forms.EmailField(max_length = 512)
    # roll_number = forms.IntegerField(
    #                  help_text = "Enter 6 digit roll number"
    #                  )
    Bio = forms.CharField(max_length = 2048)

# formulario de cadastro de novo jogo
class NewGame(forms.Form):
    Titulo_do_jogo = forms.CharField()
    Desenvolvedor = forms.CharField()
    Publicador = forms.CharField()
    Tempo_de_jogo = forms.TimeField(input_formats='%H:%M:%S')
    Completou_jogo = forms.RadioSelect()