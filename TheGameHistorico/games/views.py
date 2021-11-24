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
import io
from games.forms import NewGameForm
from games.models import Game
import users

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
    def get(self, request, *args, **kwargs): 
        game = Game.objects.filter(usuario_id=request.user.id)
        
        context = {'game': game, } 
        return render(request, 'users/paginaProfile.html', context)

@login_required
def listGames(request):
    games = Game.objects.filter(owner_id=request.user.pk).all()
    return games


def cover_crawler(title):
    ssl._create_default_https_context = ssl._create_unverified_context
    query1 = title
    query2 = query1.replace(" ", "%20")
    output = ''
    str1 = '<img src="https://vgcollect.com/images/front-box-art/'
    lenMax = len(str1)

    with urllib.request.urlopen("https://vgcollect.com/search/" + query2) as response:
        html = str(response.read())
        # seq = re.findall('\"span2 item-art\"', str(html))
        # print(seq)
        #    for i in range(len(str(html))):
        # f.write(str(seq))
        j = html.find("[NA]")
        # j = html.find("\"span2 item-art\"")
        print(j)
        k = j - 2
        for i in range(k, len(html) - lenMax):
            # print(i)
            if html.find(str1, i, i + lenMax) > 0:

                temp = html[i : i + lenMax + 20]
                urltest = temp[10 : temp.find(".jpg") + 4]
               
                print(urltest)

                picname = urllib.request.urlopen(urltest)
                file = io.BytesIO(picname.read())
                im = Image.open(file)
                output = 'games/static/games/img/'+ query1 + '.jpg'
                im.save(output)
                break
    return '/static/games/img/'+ query1 + '.jpg'

        
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
    
    
# def getGamePublicList():
#     return games

class GamePublicListView(View):
    def get(self, request, *args, **kwargs): 
        gameList = []
        games = Game.objects.all()

        for e in Game.objects.all():
            if request.GET.get("gameTitle") in e.title:
                gameList.append(e)

        if len(gameList) > 0:
            context = { 'game' : gameList }
        else:
            context = { 'game' : games }
                   
        return render(request, 'games/grid.html', context)             
        # return render(request, 'games/grid.html', context)
        
        