from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListadoLibros.as_view(), name='listado_libros'),
    path('crear/', views.CrearLibro.as_view(), name='crear_libro'),
    path('modificar/<int:pk>/', views.ModificarLibro.as_view(), name='modificar_libro'),
    path('eliminar/<int:pk>/', views.EliminarLibro.as_view(), name='eliminar_libro'),
]
