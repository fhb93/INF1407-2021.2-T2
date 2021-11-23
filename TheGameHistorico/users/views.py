from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic.base import View 
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import UpdateView, CreateView, BaseUpdateView

from games import views
import games
from users.forms import NewUserForm, BioForm
from users.models import User, Bio


# from django.contrib.auth.models import User
# class MyLoginPage(View):
#     def post(self, request, *args, **kwargs):
#         post_data = request.POST
#         user = authenticate(username=post_data['username'], password=post_data['password'])
#         print(user)
#         if user is None:
#             L.warning('Authentication error wrong credentials')
#             return HttpResponseRedirect('/')
#         else:
#             auth_login(request, user)
#             L.INFO('Authentication ok')
#             return HttpResponseRedirect('/')
#
#
#     def get(self, request, *args, **kwargs):
#         form = LoginForm()
#         context = {'form': form}
#         return render(request, 'users/login.html', context )
#
# Create your views here.
class RegisterNewUserView(View):
    def get(self, request, *args, **kwargs):
        # print(Usuario.objects.all())
        form = NewUserForm()
        context = {'formulario': form }
        return render(request, 'users/registro.html', context)
    
    def post(self, request, *args, **kwargs):
        form = NewUserForm(request.POST)
        if form.is_valid():
            # bio = form.get_bio()
            # user = form;
            user = form.save()
            user.save()
            print(user.username)
            # print(user.bio)
            
            # print(user.username)
            # Usuario.objects.create(username=form.username, password=form.password, email=form.email, bio=form.bio)
            # user.save()
            # user = form.cleaned_data.get('username')
            
            messages.success(request, 'Account was created for ' + user.username)
            return redirect('sec-paginaProfile')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'formulario': form}
            return render(request, 'users/registro.html', context)
        return
    
def verificaUsername(request): 
    username = request.GET.get('username', None) 
    resposta = { 
        'existe': User.objects.filter(username__iexact=username).exists()
        } 
    return JsonResponse(resposta)    
    
class UserListView(View): 
    def get(self, request, *args, **kwargs): 
        usuarios = User.objects.all() 
        context = { 'users': usuarios, } 
        return render(request, 'users/listaContatos.html', context) 
    
# class MyUpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView):
#     def get(self, request, pk, *args, **kwargs): 
#         form = BioForm()
#         context = { 'bioForm' : form } 

def showUserBio(request):
    bio = None
    try:
        bio = Bio.objects.get(author=request.user.id).content    
    except:
        pass
        
    return bio
 
class UserUpdateView(View): 
    def get(self, request, pk, *args, **kwargs): 
        # user = User.objects.get(pk=pk) 
       
        context = {'bioForm': BioForm, } 
        return render(request, 'users/user_form.html', context) 
     
    def post(self, request, pk, *args, **kwargs):
        if request.POST.get("voltar"):
            return HttpResponseRedirect(reverse_lazy("sec-paginaProfile")) 
        
        user = get_object_or_404(User, pk=pk)
        formulario = BioForm(request.POST) 
        # bio = get_object_or_404(Bio, author=user.id)
        if formulario.is_valid(): 
            try:
                bio = Bio.objects.get(author=user)
                userTemp = BioForm(request.POST, instance=bio).save(commit=False)
                userTemp.author = request.user   
                userTemp.save()
            except:
                userTemp = formulario.save(commit=False)
                userTemp.author = request.user   
                userTemp.save()
        else: 
            bio = Bio.objects.get(author=user)
            formulario = BioForm(instance=bio)
            context = {'bioForm': formulario, } 
            return render(request, 'users/user_form.html', context)
    
            
        return HttpResponseRedirect(reverse_lazy("sec-paginaProfile")) 
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
            # games = Game.objects.all()
            games = views.listGames(request)
            bio = showUserBio(request)
            context = { 'games': games, 'bio' : bio} 
            print(bio)
            return render(request,'users/paginaProfile.html', context)     
    
    return render(request, 'users/paginaProfile.html')





