from django.shortcuts import render, redirect
from django.views.generic.base import View 

from users.models import Usuario
from users.forms import NewUser


# Create your views here.
class UserListView(View): 
    def get(self, request, *args, **kwargs): 
        usuarios = Usuario.objects.all() 
        context = { 'users': usuarios, } 
        return render(request, 'users/listaContatos.html', context) 
    


def registraUsuario(request):
    if request.method == "POST":
        formulario = NewUser(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
        
    else:
        formulario = NewUser()
        
    contexto = {'formulario' : formulario, }
    return render(request, "users/registro.html", contexto)

def paginaProfile(request):
    return render(request, 'users/paginaProfile.html')