from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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

# Vista para el perfil de usuario
@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html')

# Vista para editar el perfil de usuario
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario = UserChangeForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')
    else:
        formulario = UserChangeForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})

# Vista para cambiar la contraseña (usando la vista genérica de Django)
class CambiarContraseña(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'usuarios/cambiar_contraseña.html'
    success_url = reverse_lazy('perfil')
