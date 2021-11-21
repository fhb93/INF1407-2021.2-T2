from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, _get_queryset 
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
    def get_queryset(self, request):
        return Game.objects.filter(request.username) #.order_by('')

    # def get(self, request, *args, **kwargs): 
    #     # games = User.objects.get(username='t123').game_set.all() #objects.all()
    #     games = Game.objects.all() #(self, request)
    #     context = { 'listaGames': games, } 
    #     return render(request,'users/paginaProfile.html', context)
    #
    def get(self, request, *args, **kwargs): 
        game = Game.objects.all() 
        context = {'game': game, } 
        return render(request, 'users/paginaProfile.html', context)


        
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
            return HttpResponseRedirect(reverse_lazy("sec-paginaProfile")) 
        else: 
            context = {'game': formulario, } 
            return render(request, 'games/atualizaGame.html', context)
        
class GameDeleteView(View): 
    def get(self, request, pk, *args, **kwargs): 
        game = Game.objects.get(pk=pk) 
        context = {'game': game, } 
        return render(request, 'games/apagaGame.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        if request.POST.get("remove-btn"):
            game = Game.objects.get(pk=pk)
            game.delete() 
            print("Removendo o jogo", pk) 
            
        return HttpResponseRedirect(reverse_lazy("sec-paginaProfile")) 