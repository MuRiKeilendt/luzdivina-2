from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.Home,name='home'), 
    path('boda/',views.Listado,name='boda'),
    path('bautizo/',views.Bautiso, name='bautizo'),
    path('comunion/',views.Comunione, name='comunion'),
    path('login/',views.Login,name="login"),
    path('parroquia',views.FormularioParroquia,name="parroquia"),
    path('indexLogin/',views.IndexLogin,name="indexLogin"),
    path('comunidad/',views.FormularioComunidad,name="comunidad"),
    path('agente/',views.FormularioAgente,name="agente"),
    path('coordinador/',views.FormularioCoordinador,name="coordinador"),
    path('ministro/',views.FormularioMinistro,name="ministro")
]