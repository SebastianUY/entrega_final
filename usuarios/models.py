from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modelo que extiende el usuario de Django para almacenar el avatar
class Perfil(models.Model):
    # Enlace uno a uno con el modelo de Usuario de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campo para almacenar la imagen del avatar. 
    # Guarda las imágenes en la carpeta MEDIA_ROOT/avatares/
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Señal para crear el Perfil automáticamente al crear un Usuario
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

# Señal para guardar el Perfil automáticamente al guardar un Usuario
@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()
