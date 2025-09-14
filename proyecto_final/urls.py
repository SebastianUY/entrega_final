"""
URL configuration for proyecto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libros.views import inicio, crear_libro, listado_libros, eliminar_libro, modificar_libro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path('listado-libros/', listado_libros, name='listado_libros'),
    path('eliminar-libro/<int:id_libro>/', eliminar_libro, name='eliminar_libro'),
    path('modificar-libro/<int:id_libro>/', modificar_libro, name='modificar_libro'),
]