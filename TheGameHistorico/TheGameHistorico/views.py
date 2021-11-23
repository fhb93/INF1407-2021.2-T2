'''
Created on Nov 19, 2021

@author: felipe
'''
from django.shortcuts import render 

import games
from django.http.response import HttpResponseRedirect


# from django.http import HttpResponse
# from TheGameHistorico.forms import NewUser
# Create your views here. 
def home(request): 
    return render(request, 'index.html')
    # return HttpResponse('Alô mundo!')
    
def homeSec(request):
    return render(request, 'index.html')
