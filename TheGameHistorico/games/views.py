from django.http.response import HttpResponse
from django.shortcuts import render

from games.forms import NewGameForm


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