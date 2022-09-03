from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
    path('', views.Home,name='Home'),
    path('Aboutus', views.Aboutus,name='Aboutus'),
    path('Contactus',views.Contactus,name='Contactus'),
    path('Team',views.Team,name='Team'),
   
]
