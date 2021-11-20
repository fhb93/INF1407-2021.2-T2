from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404 
from django.urls.base import reverse_lazy
from django.views.generic.base import View 
from games.forms import NewGameForm
from games.models import Game
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
        print(games) 
        context = { 'games': games, } 
        return render( 
            request,  
            'games/listaGames.html',  
            context)
        
        
class GameCreateView(View): 
    def get(self, request, *args, **kwargs): 
        context = { 'formularioGame': NewGameForm, } 
        return render(request, "games/registroGame.html", context) 
     
    def post(self, request, *args, **kwargs): 
        formulario = NewGameForm(request.POST)
         
        if formulario.is_valid(): 
            game = formulario.save()
            game.save() 
            # Game.objects.create(game)
            return HttpResponseRedirect(reverse_lazy("sec-paginaProfile"))
        else:
            formulario = NewGameForm()
        
        contexto = {'formularioGame' : formulario, }
        return render(request, "users/paginaProfile.html", contexto)

        
 
class GameUpdateView(View): 
    def get(self, request, pk, *args, **kwargs): 
        game = Game.objects.get(pk=pk) 
        formulario = NewGameForm(instance=game) 
        context = {'game': formulario, } 
        return render(request, 'games/atualizaGame.html', context) 
     
    def post(self, request, pk, *args, **kwargs): 
        pessoa = get_object_or_404(Game, pk=pk) 
        formulario = NewGameForm(request.POST, instance=pessoa) 
        if formulario.is_valid(): 
            pessoa = formulario.save() 
            pessoa.save() 
            return HttpResponseRedirect(reverse_lazy("lista-jogos")) 
        else: 
            context = {'game': formulario, } 
            return render(request, 'games/atualizaGame.html', context) 