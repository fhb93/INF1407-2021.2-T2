from django.shortcuts import render

# Create your views here.
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