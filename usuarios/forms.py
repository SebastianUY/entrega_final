from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

# Obtener el modelo de usuario activo (User por defecto o el modelo personalizado)
User = get_user_model()

class CustomUserEditForm(forms.ModelForm):
    """
    Formulario para la edición del perfil de usuario.
    Hereda de ModelForm y usa el modelo de usuario.
    """
    class Meta:
        model = User
        # Lista de campos que quieres que el usuario pueda editar
        fields = ['username', 'first_name', 'last_name', 'email']