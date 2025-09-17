from django.urls import path
from .views import ListadoLibros, CrearLibro, ModificarLibro, EliminarLibro

urlpatterns = [
    # La plantilla usa 'pk', así que el patrón de URL debe usar 'pk' también.
    path('listado-libros/', ListadoLibros.as_view(), name='listado_libros'),
    path('crear-libro/', CrearLibro.as_view(), name='crear_libro'),
    path('modificar-libro/<int:pk>/', ModificarLibro.as_view(), name='modificar_libro'),
    path('eliminar-libro/<int:pk>/', EliminarLibro.as_view(), name='eliminar_libro'),
]
