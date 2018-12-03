from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'core/index.html')

def Formulario(request):
    return render(request,'core/formulario.html')

def Bautizo(request):
    return render(request,'core/formularioBautizo.html')

def Comunion(request):
    return render(request,'core/formularioComunion.html')