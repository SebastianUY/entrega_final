from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CustomUserEditForm 

# Vista para el registro de usuarios
def registro_usuario(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': formulario})

# Vista para el perfil de usuario (Simple)
@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html')


# Vista para editar el perfil de usuario (Ahora usa CustomUserEditForm)
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Usamos tu formulario personalizado para guardar los datos.
        formulario = CustomUserEditForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            # Redirige al perfil después de guardar
            return redirect('perfil')
    else:
        # Pasa los datos actuales del usuario al formulario en GET, usando tu formulario personalizado.
        formulario = CustomUserEditForm(instance=request.user)
        
    # Renderiza la plantilla de edición, pasando el formulario
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})

# Vista para cambiar la contraseña (usando la vista genérica de Django)
class CambiarContraseña(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'usuarios/cambiar_contrasena.html'
    success_url = reverse_lazy('password_change_done') 
