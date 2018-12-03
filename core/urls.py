from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.Home,name='home'), 
    path('boda/',views.Formulario,name='boda'),
    path('bautizo/',views.Bautizo, name='bautizo'),
    path('comunion/',views.Comunion, name='comunion'),
]