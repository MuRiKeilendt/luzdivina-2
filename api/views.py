from rest_framework import generics
from .serializers import ComunidadSerializers, BodaSerializers, BautizoSerializers, ComunionSerializers, PersonaSerializers
from core.models import Comunidad, Boda, Bautizo, Comunion, Persona
# Create your views here.
class ComunidadLista(generics.ListCreateAPIView):
    queryset = Comunidad
    serializer_class= ComunidadSerializers

class ComunidadDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comunidad
    serializer_class=ComunidadSerializers

class BodaLista(generics.ListCreateAPIView):
    queryset = Boda
    serializer_class= BodaSerializers

class BodaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boda
    serializer_class= BodaSerializers    

class BautizoLista(generics.ListCreateAPIView):
    queryset = Bautizo
    serializer_class= BautizoSerializers

class BautizoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bautizo
    serializer_class= BautizoSerializers  

class ComunionLista(generics.ListCreateAPIView):
    queryset = Comunion
    serializer_class= ComunionSerializers

class ComunionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comunion
    serializer_class= ComunionSerializers  

class PersonaLista(generics.ListCreateAPIView):
    queryset = Persona
    serializer_class= PersonaSerializers

class PersonaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona
    serializer_class= PersonaSerializers