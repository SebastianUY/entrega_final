from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro
from .forms import FormularioLibro

# Vista de listado de libros
class ListadoLibros(ListView):
    model = Libro
    template_name = 'listado_libros.html'
    context_object_name = 'libros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['libros']:
            context['mensaje'] = "No hay libros aún. ¡Sé el primero en agregar uno!"
        return context

# Vista para crear un libro
class CrearLibro(CreateView):
    model = Libro
    form_class = FormularioLibro
    template_name = 'crear_libro.html'
    success_url = reverse_lazy('listado_libros')

# Vista para modificar un libro
class ModificarLibro(UpdateView):
    model = Libro
    form_class = FormularioLibro
    template_name = 'modificar_libro.html'
    success_url = reverse_lazy('listado_libros')
    # Esta variable de contexto coincide con el nombre en tu plantilla
    context_object_name = 'formulario'

# Vista para eliminar un libro
class EliminarLibro(DeleteView):
    model = Libro
    template_name = 'eliminar_libro.html'
    success_url = reverse_lazy('listado_libros')
