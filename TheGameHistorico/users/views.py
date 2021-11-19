from django.shortcuts import render

# Create your views here.
from users.models import Usuario 
from django.views.generic.base import View 

class UserListView(View): 
    def get(self, request, *args, **kwargs): 
        usuarios = Usuario.objects.all() 
        context = { 'users': usuarios, } 
        return render( 
            request,  
            'users/listaContatos.html', context) 