'''
Created on Nov 20, 2021

@author: felipe
''' 
from django.urls.conf import include, path

from games import views


app_name='games'

urlpatterns = [ 
     path('templates/games/', views.registraJogo, 'registrar-novo-jogo'),
    # path('games/newGame/', views.registraJogo, name='registrar-novo-jogo'), 
]