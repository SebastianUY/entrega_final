from django import forms
from .models import Libro

# Usamos ModelForm para crear un formulario a partir del modelo Libro.
# Esto nos evita tener que definir cada campo manualmente.
class FormularioCreacionLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion']