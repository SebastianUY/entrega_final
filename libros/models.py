from django.db import models

# Modelo para representar un libro.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    # Campo para la fecha de publicación, como lo has indicado
    fecha_publicacion = models.IntegerField()
    # Nuevo campo para la imagen de portada
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    
    # Este método define cómo se mostrará el objeto en el panel de administración de Django.
    def __str__(self):
        return f'{self.titulo} ({self.autor})'