"""TheGameHistorico URL Configuration

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
    PasswordChangeDoneView
from django.urls import path
from django.urls.base import reverse_lazy
from django.urls.conf import include

import users
import games

from . import views


urlpatterns = [
    path('', views.homeSec, name='sec-home'),
    path('admin/', admin.site.urls),
    path("users/", include ('users.urls')),
    path('games/', include('games.urls')),
    path('games/adicionarJogo', games.views.GameCreateView.as_view(), name='registrar-novo-jogo'),
    path('games/listar/', games.views.GameListView.as_view(), name='lista-games'), 
    path('templates/', views.homeSec, name='nav-bar-home'),
    path('accounts/users/', users.views.registraUsuario, name = 'sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='users/login.html'), name='sec-login',),
    # path('accounts/profile/', users.views.paginaProfile, name='sec-paginaProfile', ),
    path('accounts/profile/', users.views.paginaProfile, name='sec-paginaProfile'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home')), name="sec-logout"),
    path('accounts/trocaSenha/', PasswordChangeView.as_view(template_name='users/password_change_form.html', success_url = reverse_lazy('sec-passwordDone')), name='sec-passwordChange'),
    path('accounts/senhaTrocada/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html', ), name='sec-passwordDone'),
]
