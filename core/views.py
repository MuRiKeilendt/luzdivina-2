from django.shortcuts import render
from .models import Comunidad, Boda, Bautizo, Comunion, Comunidadcatolica

# Create your views here.


def Home(request):
    return render(request, 'core/index.html')


def Bautiso(request):
    listado = Bautizo.objects.all()
    comunidadCatolica = Comunidadcatolica.objects.all()
    return render(request, 'core/formularioBautizo.html', {'listado':listado,'comunidadCatolica':comunidadCatolica})


def Formulario(request):
    lt = Comunidad.objects.all()
    if request.POST:
        nombreNovia = request.POST["nombreNovia"]
        nombreNovio = request.POST["nombreNovio"]
        numeroContacto = request.POST["numeroContacto"]
        emailContacto = request.POST["emailContacto"]
        tipoParroquia = request.POST["tipoParroquia"]

        obj_tipo = Comunidad.objects.get(id=tipoParroquia)

        boda = Boda(
            nombreNovia=nombreNovia,
            nombreNovio=nombreNovio,
            numeroContacto=numeroContacto,
            emailContacto=emailContacto,
            tipoParroquia=obj_tipo
        )

        boda.save()
    return render(request, 'core/formulario.html', {'tipoParroquias': lt, 'mensaje': 'Registrado Correctamente'})

    return render(request, 'core/formulario.html', {'tipoParroquias': lt})


def Comunione(request):
    listado = Comunion.objects.all()
    comunidadCatolica = Comunidadcatolica.objects.all()
    return render(request, 'core/formularioComunion.html', {'listado':listado,'comunidadCatolica':comunidadCatolica})


def Listado(request):
    listado = Boda.objects.all()
    comunidadCatolica = Comunidadcatolica.objects.all()
    return render(request, 'core/formulario.html', {'listado':listado,'comunidadCatolica':comunidadCatolica})

