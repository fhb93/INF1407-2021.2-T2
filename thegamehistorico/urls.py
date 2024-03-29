"""thegamehistorico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from django.urls.base import reverse_lazy
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.views.generic.edit import UpdateView

import games
import users
from . import views


urlpatterns = [
    path('', views.homeSec, name='sec-home'),
    path('admin/', admin.site.urls),
    path("users/", include ('users.urls')),
    path('games/', include('games.urls')),
    path('games/listaPublica/', games.views.GamePublicListView.as_view(), name='lista-publica-games'),
    path('games/adicionarJogo/', games.views.GameCreateView.as_view(), name='registrar-novo-jogo'),
    path('games/atualizarJogo/<int:pk>/', games.views.GameUpdateView.as_view(), name='atualizar-jogo'),
    path('games/apagarJogo/<int:pk>/', games.views.GameDeleteView.as_view(), name='remover-jogo'),
    path('games/listar/', games.views.GameListView.as_view(), name='lista-games'), 
    path('templates/', views.homeSec, name='nav-bar-home'),
    path('accounts/users/', users.views.RegisterNewUserView.as_view(), name = 'sec-registro'),
    path('sobreoSite/', views.sobre, name='sobre-o-site'),
    path('exibeCharsRest/', users.views.exibeCharsRestantes, name='exibeCharsRest'),
    path('verificaUsername/', users.views.verificaUsername, name='verificaUsername'),
    path('accounts/login/', LoginView.as_view(template_name='users/login.html'), name='sec-login',), # was LoginView.as_view(template_name='users/login.html', )
    # path('accounts/profile/', users.views.paginaProfile, name='sec-paginaProfile', ),
    path('accounts/profile/', users.views.paginaProfile, name='sec-paginaProfile'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home')), name="sec-logout"),
    path('accounts/trocaSenha/', PasswordChangeView.as_view(template_name='users/password_change_form.html', success_url = reverse_lazy('sec-passwordDone')), name='sec-passwordChange'),
    path('accounts/senhaTrocada/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html', ), name='sec-passwordDone'),
    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico')),
    path('accounts/password_reset/', PasswordResetView.as_view( 
           template_name='users/password_reset_form.html',  
           success_url=reverse_lazy('sec-password_reset_done'), 
           email_template_name='users/password_reset_email.html', 
           subject_template_name='users/password_reset_subject.txt', 
           from_email='felipe@philisoftstudio.com', 
         ), name='password_reset'), 
     
    path('accounts/password_reset_done/', PasswordResetDoneView.as_view( 
           template_name='users/password_reset_done.html', 
         ), name='sec-password_reset_done'), 
     
    path('accounts/password_reset_confirm/<uidb64>/<token>/',  
         PasswordResetConfirmView.as_view( 
           template_name='users/password_reset_confirm.html',  
           success_url=reverse_lazy('sec-password_reset_complete'), 
         ), name='password_reset_confirm'), 
     
    path('accounts/password_reset_complete/', PasswordResetCompleteView.as_view( 
           template_name='users/password_reset_complete.html' 
         ), name='sec-password_reset_complete'),
    
    path('accounts/terminaRegistro/<int:pk>/', users.views.UserUpdateView.as_view(), name='sec-completaDadosUsuario'),
    # path('accounts/profile/', users.views.showUserBio, name='sec-userBio')
]
