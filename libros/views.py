from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import FormularioCreacionLibro

def inicio(request):
    """
    Vista de inicio que renderiza la plantilla de bienvenida.
    """
    return render(request, 'inicio.html')

def crear_libro(request):
    mensaje_exito = ""
    formulario = FormularioCreacionLibro()
    
    if request.method == "POST":
        formulario = FormularioCreacionLibro(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje_exito = "¡Has creado un nuevo libro con éxito!"
            formulario = FormularioCreacionLibro()

    return render(request, 'crear_libro.html', {'formulario': formulario, 'mensaje_exito': mensaje_exito})

def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listado_libros.html', {'libros': libros})

def eliminar_libro(request, id_libro):
    libro = get_object_or_404(Libro, id=id_libro)
    libro.delete()
    return redirect('listado_libros')

def modificar_libro(request, id_libro):
    libro = get_object_or_404(Libro, id=id_libro)
    
    if request.method == "POST":
        formulario = FormularioCreacionLibro(request.POST, instance=libro)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado_libros')
    else:
        formulario = FormularioCreacionLibro(instance=libro)
    
    return render(request, 'modificar_libro.html', {'formulario': formulario})
