from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro
from .forms import FormularioCreacionLibro

def inicio(request):
    """
    Vista de inicio que renderiza la plantilla de bienvenida.
    """
    return render(request, 'inicio.html')

class CrearLibro(CreateView):
    """
    Vista basada en clase para crear un nuevo libro.
    """
    model = Libro
    form_class = FormularioCreacionLibro
    template_name = 'crear_libro.html'
    success_url = reverse_lazy('listado_libros')

class ListadoLibros(ListView):
    """
    Vista basada en clase para mostrar una lista de libros.
    """
    model = Libro
    template_name = 'listado_libros.html'
    context_object_name = 'libros'

class ModificarLibro(UpdateView):
    """
    Vista basada en clase para modificar un libro existente.
    """
    model = Libro
    form_class = FormularioCreacionLibro
    template_name = 'modificar_libro.html'
    success_url = reverse_lazy('listado_libros')

class EliminarLibro(DeleteView):
    """
    Vista basada en clase para eliminar un libro.
    """
    model = Libro
    # Indica la ruta del template que se renderizará para la confirmación
    template_name = 'libro_confirm_delete.html'
    # Redirecciona a la URL de listado_libros después de eliminar con éxito
    success_url = reverse_lazy('listado_libros')
