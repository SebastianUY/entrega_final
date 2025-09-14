from django.urls import path
from . import views

urlpatterns = [
    # Asegúrate de que este nombre sea exactamente 'listado_libros'
    path('crear-libro/', views.crear_libro, name='crear_libro'),
    path('listado-libros/', views.listado_libros, name='listado_libros'),
]