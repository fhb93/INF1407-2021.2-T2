'''
Created on Nov 19, 2021

@author: felipe
'''
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls.base import reverse_lazy
from django.urls.conf import path, include 

import games
from users import views 
from games.views import GameListView


app_name = "users" 
 
# urlpatterns = [ 
#     path('list/', views.UserListView.as_view(),  
#         name='lista-usuarios'), 
#     path('', views.UserListView.as_view(),  
#         name='home-usuarios'), 
#     ] 

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', Homepage.views.home, name='sec-home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/users/', views.registraUsuario, name = 'sec-registro'),
    path('accounts/login/', LoginView.as_view(template_name='users/templates/login.html'), name='sec-login',),
    # path('accounts/profile/', GameListView.as_view(), name='games', ),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home')), name="sec-logout"),
    path('accounts/trocaSenha/', PasswordChangeView.as_view(template_name='users/password_change_form.html', success_url = reverse_lazy('sec-passwordDone')), name='sec-passwordChange'),
    path('accounts/senhaTrocada/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html', ), name='sec-passwordDone'),
  

]