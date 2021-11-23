import re
import urllib
import ssl



from django.conf import settings
from django.contrib import sessions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import exceptions
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, _get_queryset 
from django.urls.base import reverse_lazy
from django.views.generic.base import View 
from PIL import Image
from games.forms import NewGameForm
from games.models import Game
import users

ssl._create_default_https_context = ssl._create_unverified_context
# Create your views here.
# def registraJogo(request):
#     # return HttpResponse("ola")
#     if request.method == "POST":
#         formulario = NewGameForm(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             titulo = formulario.Titulo_do_jogo
#             # list = get_cover(titulo)
#             return HttpResponse(str(list)) #redirect('sec-home')
#     else:
#         formulario = NewGameForm()
#
#
#     contexto = {'formularioGame' : formulario, }
#     return render(request, "games/registroGame.html", contexto)
class GameListView(LoginRequiredMixin, View): 
    def get_queryset(self, request):
        return Game.objects.filter(request.username) #.order_by('')

    # def get(self, request, *args, **kwargs): 
    #     # games = User.objects.get(username='t123').game_set.all() #objects.all()
    #     games = Game.objects.all() #(self, request)
    #     context = { 'listaGames': games, } 
    #     return render(request,'users/paginaProfile.html', context)
    #
    def get(self, request, *args, **kwargs): 
        game = Game.objects.filter(usuario_id=request.user.id)
        
        context = {'game': game, } 
        return render(request, 'users/paginaProfile.html', context)

@login_required
def listGames(request):
    games = Game.objects.filter(owner_id=request.user.pk).all()
    return games


def cover_crawler(game_title):
    query1 = game_title
    query2 = query1.replace(" ", "%20")
    # out = []
    with urllib.request.urlopen("https://vgcollect.com/search/" + query2) as response:
        html = response.read()
        seq = re.findall('\[NA\]</a>', str(html))
        # print(seq)
        #    for i in range(len(str(html))):
        f = open(query1 + ".txt", "w")
        f.write(str(seq))
        
        for i in range(0, len(str(html))):
            if("[NA]</a> - Official Release" == str(html)[i : i + len("[NA]</a> - Official Release")]):
                input = str(html)[i : i + 1200]
                # url1 = "https://vgcollect.com/item/"
                url1 = 'https://vgcollect.com/images/front-box-art/'
                url2 = '.jpg'
                
                try:
                    index1 = input.index(url1)
                    index2 = input.index(url2)
                    # f.write(str(input)[index : len(url1)])
                    # f.write("\n\n\n\n")
                    # print(str(input)[index1 : index2 + 4])
                    picture = Image.open(str(input)[index1 : index2 + 4])
                    picture.save('static/games/img/' + game_title + url2)
                    # f.write("\n" + str(input)[index1 : index2 + 4] + "\n\n")
                    # out.append(str(input)[index1 : index2 + 4])
                except:
                    continue
        f.close()
    return str('static/games/img/' + game_title + url2)

        
class GameCreateView(LoginRequiredMixin, View): 
    def get(self, request, *args, **kwargs): 
        print(request.user.username)
        try:
            print(request.user)
        except:
            print('não achei')
        context = { 'formularioGame': NewGameForm, } 
        
        return render(request, "games/registroGame.html", context) 
     
    def post(self, request, *args, **kwargs): 
        formulario = NewGameForm(request.POST)
         
        if formulario.is_valid(): 
            game = formulario.save(commit=False)
            game.owner = users.views.User.objects.get(username=request.user.username)
            # game.usuario_id = request.user
            # game.usuario_id = Usuario.objects.get(usuario_id=request.user.pk)
            print(str(game.owner))
            game.cover_path = cover_crawler(game.title)
            game.save() 
            # Game.objects.create(game)
            return HttpResponseRedirect(reverse_lazy("sec-paginaProfile"))
        else:
            formulario = NewGameForm()
        
        contexto = {'formularioGame' : formulario, }
        return render(request, "users/paginaProfile.html", contexto)

        
 
class GameUpdateView(LoginRequiredMixin, View): 
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
            pessoa.cover_path = cover_crawler(pessoa.title) 
            pessoa.save()
            return HttpResponseRedirect(reverse_lazy("sec-paginaProfile")) 
        else: 
            context = {'game': formulario, } 
            return render(request, 'games/atualizaGame.html', context)
        
class GameDeleteView(LoginRequiredMixin, View): 
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
    
    
def getGamePublicList():
    games = Game.objects.all()
    return games

class GamePublicListView(View):
    def get(self, request, *args, **kwargs): 
        context = { 'game' : getGamePublicList() }
        return render(request, 'games/grid.html', context)
        
        