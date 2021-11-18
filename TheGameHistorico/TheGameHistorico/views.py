from django.shortcuts import redirect, render 
from django.http import HttpResponse
from TheGameHistorico.covercrawler import get_cover
from TheGameHistorico.forms import NewGameForm, NewUser


 
# Create your views here. 
 
def home(request): 
    return render(request, 'TheGameHistorico/index.html')
    # return HttpResponse('Alô mundo!')


# def segundaPagina(request): 
#     # processamento antes de mostrar 
#     # a segunda página 
#     return render(request, 'MeuApp/segunda.html')

def homeSec(request):
    return render(request, 'registro/homeSec.html')

def registraJogo(request):
    if request.method == "POST":
        formulario = NewGameForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            titulo = formulario.Titulo_do_jogo
            list = get_cover(titulo)
            return HttpResponse(str(list)) #redirect('sec-home')
    else:
        formulario = NewGameForm()

    
    contexto = {'formularioGame' : formulario, }
    return render(request, "jogo/registroGame.html", contexto)


def registraUsuario(request):
    if request.method == "POST":
        formulario = NewUser(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
        
    else:
        formulario = NewUser()
        
    contexto = {'formulario' : formulario, }
    return render(request, "registro/registro.html", contexto)

def paginaProfile(request):
    return render(request, 'registro/paginaProfile.html')