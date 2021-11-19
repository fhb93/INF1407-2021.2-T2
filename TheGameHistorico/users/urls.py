'''
Created on Nov 19, 2021

@author: felipe
'''
from django.urls.conf import path 

from users import views 


app_name = "users" 
 
urlpatterns = [ 
    path('list/', views.UserListView.as_view(),  
        name='lista-usuarios'), 
    path('', views.UserListView.as_view(),  
        name='home-usuarios'), 
    ] 