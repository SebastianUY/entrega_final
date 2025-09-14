from django.shortcuts import render

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista "Acerca de Mí"
def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')