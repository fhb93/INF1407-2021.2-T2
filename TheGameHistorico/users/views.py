from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.base import View 
from django.views.generic.edit import UpdateView

import games
from games.models import Game
from users.forms import NewUser
from users.models import Usuario


# Create your views here.
class RegisterNewUserView(View):
    def get(self, request, *args, **kwargs):
        form = NewUser()
        self.verificaUsername(request)
        context = {'formulario': form}
        return render(request, 'users/registro.html', context)
    
    def post(self, request, *args, **kwargs):
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            # user = form.cleaned_data.get('username')
            usuario = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + usuario)
            return redirect('sec-paginaProfile')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'formulario': form}
            return render(request, 'users/registro.html', context)
        return
    def verificaUsername(self, request): 
        username = request.GET.get("username", None) 
        resposta = { 
            'existe': User.objects.filter(username__iexact=username).exists()
            } 
        return JsonResponse(resposta)    
    
class UserListView(View): 
    def get(self, request, *args, **kwargs): 
        usuarios = Usuario.objects.all() 
        context = { 'users': usuarios, } 
        return render(request, 'users/listaContatos.html', context) 
    
class MyUpdateView(View): 
    def get(self, request, pk, *args, **kwargs): 
        if request.user.id == pk: 
            return super().get(request, pk, args, kwargs) 
        else: 
            return redirect('sec-home')
        
#
# def registraUsuario(request):
#     if request.method == 'GET':
#         form = NewUser()
#         context = {'formulario': form}
#         return render(request, 'users/registro.html', context)
#     if request.method == 'POST':
#
#

    
    # if request.method == "POST":
    #     formulario = NewUser(request.POST)
    #     if formulario.is_valid():
    #         user = formulario.save()
    #         user.save()
    #         # User.objects.get(username=username)
    #         # return render(request, 'users/paginaProfile.html', {'user' : user})
    #         return login(request, user=user)
    #
    #
    # return render(request, "users/registro.html", context)
@login_required
def paginaProfile(request):
    if request.method == "GET":
        if request.user.is_authenticated == True:
            games = Game.objects.all()
            context = { 'games': games, } 
            return render(request,'users/paginaProfile.html', context)     
    
    return render(request, 'users/paginaProfile.html')





