from django import forms
from django.contrib.auth.forms import UserCreationForm
   
# formulario de cadastro
class NewUser(UserCreationForm):
    Email = forms.EmailField(max_length = 512)
    # roll_number = forms.IntegerField(
    #                  help_text = "Enter 6 digit roll number"
    #                  )
    Bio = forms.CharField(max_length = 2048)
