from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.Home,name='home'), 
    path('formulario/',views.Formulario,name='formulario'),   
]