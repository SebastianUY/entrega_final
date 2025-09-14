from django.shortcuts import render, redirect
from .forms import FormularioCreacionLibro
from .models import Libro

def crear_libro(request):
    """
    Vista para manejar la creación de nuevos libros.
    """
    mensaje_exito = ""
    formulario = FormularioCreacionLibro()

    if request.method == "POST":
        formulario = FormularioCreacionLibro(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje_exito = "¡Libro agregado correctamente!"
            # Redirecciona a la página de listado después de guardar.
            return redirect('listado_libros') 

    return render(request, 'crear_libro.html', {
        'formulario': formulario, 
        'mensaje_exito': mensaje_exito
    })

def listado_libros(request):
    """
    Vista para mostrar un listado de todos los libros.
    """
    # Obtiene todos los objetos de la base de datos para el modelo Libro.
    libros = Libro.objects.all()
    # Pasa el listado de libros a la plantilla HTML.
    return render(request, 'listado_libros.html', {'libros': libros})