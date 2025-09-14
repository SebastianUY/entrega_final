from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.IntegerField()
    
    # Este método define cómo se mostrará el objeto en el panel de administración de Django.
    def __str__(self):
        return f'{self.titulo} ({self.autor})'