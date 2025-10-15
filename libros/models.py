from django.db import models

# Modelo para representar un libro.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) 
    fecha_publicacion = models.IntegerField(null=True, blank=True) 
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.titulo} ({self.autor})'
