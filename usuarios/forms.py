from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

# Creamos un formulario personalizado para editar el usuario.
class FormularioEdicionUsuario(UserChangeForm):
    # La clase Meta le dice al formulario qué modelo usar y qué campos mostrar.
    class Meta:
        model = User
        # Excluimos la contraseña del formulario, que se debe cambiar con un formulario separado por seguridad.
        exclude = ['password']
        fields = ['username', 'first_name', 'last_name', 'email']