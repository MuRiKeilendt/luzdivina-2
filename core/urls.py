from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.Home,name='home'), 
    path('boda/',views.Listado,name='boda'),
    path('bautizo/',views.Bautiso, name='bautizo'),
    path('comunion/',views.Comunione, name='comunion'),
]