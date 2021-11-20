from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import View 

import games
from games.models import Game
from users.forms import NewUser
from users.models import Usuario


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
            return redirect('sec-paginaProfile')
    
    context = { 'formulario': NewUser, } 
    
    return render(request, "users/registro.html", context)
    # return render("sec-registro")

def paginaProfile(request):
    if request.method == "GET":
        games = Game.objects.all()
        context = { 'games': games, } 
        return render(request,'users/paginaProfile.html', context)     
        
    
    return render(request, 'users/paginaProfile.html')