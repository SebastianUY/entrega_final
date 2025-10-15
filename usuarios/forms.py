from django import forms
from django.contrib.auth.forms import UserChangeForm # Importación necesaria para editar el modelo User
from django.contrib.auth.models import User # Importación necesaria
from .models import Perfil

# Formulario para gestionar el Avatar del modelo Perfil
class FormularioPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        # Solo necesitamos el campo 'avatar' en este formulario
        fields = ['avatar']

        # Opcional: Ayuda visual para el usuario
        labels = {
            'avatar': 'Seleccionar Avatar',
        }

# NUEVO FORMULARIO: Versión personalizada de UserChangeForm
# Se utiliza para editar los datos del usuario (nombre, apellido, email, username) sin exponer campos sensibles.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # Definimos explícitamente solo los campos que queremos que el usuario edite
        fields = ('username', 'first_name', 'last_name', 'email')
        
    # Sobrescribimos el constructor para asegurarnos de que el campo de contraseña
    # no se muestre, aunque ya lo excluimos en 'fields'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']