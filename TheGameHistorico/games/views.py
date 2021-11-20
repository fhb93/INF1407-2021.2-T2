from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import View 

from games.forms import NewGameForm
from games.models import Game


# from games.forms import NewGameForm
# Create your views here.
def registraJogo(request):
    # return HttpResponse("ola")
    if request.method == "POST":
        formulario = NewGameForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            titulo = formulario.Titulo_do_jogo
            # list = get_cover(titulo)
            return HttpResponse(str(list)) #redirect('sec-home')
    else:
        formulario = NewGameForm()
    
    
    contexto = {'formularioGame' : formulario, }
    return render(request, "games/registroGame.html", contexto)


class GameListView(View): 
    def get(self, request, *args, **kwargs): 
        games = Game.objects.all() 
        context = { 'jogos': games, } 
        return render( 
            request,  
            'games/listaGames.html',  
            context)
        
        
class GameCreateView(View): 
    def get(self, request, *args, **kwargs): 
        context = { 'formulario': NewGameForm, } 
        return render(request, "games/registroGame.html", context) 
     
    def post(self, request, *args, **kwargs): 
        formulario = NewGameForm(request.POST) 
        if formulario.is_valid(): 
            contato = formulario.save() 
            contato.save() 
            return HttpResponseRedirect(reverse_lazy("games:lista-jogos")) 