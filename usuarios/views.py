from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
# Importamos 'View' para manejar formularios múltiples, y 'UpdateView' si se necesita en otro sitio.
from django.views import View 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

# Importamos los formularios personalizados
from .models import Perfil # Necesario para obtener la instancia de Perfil
from .forms import FormularioPerfil, CustomUserChangeForm # Los formularios para User y Perfil

# Vista para el registro de usuarios (FBV)
def registro_usuario(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()
    # Aseguramos que la clave de contexto sea 'formulario' como pide la plantilla
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

# Vista para el perfil de usuario (Solo visualización)
@login_required
def perfil(request):
    # Ya no procesa el formulario de avatar aquí; es solo para mostrar los datos.
    # CRÍTICO: Obtenemos la instancia de Perfil para que la plantilla acceda al avatar.
    perfil_instancia = request.user.perfil
    return render(request, 'usuarios/perfil.html', {'object': perfil_instancia})

# Vista para cambiar la contraseña
class CambiarContraseña(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'usuarios/cambiar_contrasena.html'
    success_url = reverse_lazy('perfil')

# VISTA CRÍTICA: Para editar los campos del modelo User y el Perfil (Avatar)
@method_decorator(login_required, name='dispatch')
class EditarPerfil(View):
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('perfil')

    # Función auxiliar para inicializar formularios
    def get_context_data(self, user_form=None, avatar_form=None):
        user = self.request.user
        context = {}
        
        # 1. Formulario de datos de usuario (Usamos el CustomUserChangeForm para excluir la contraseña)
        context['form'] = user_form or CustomUserChangeForm(instance=user)
        
        # 2. Formulario de avatar (CRÍTICO: Pasar la instancia de Perfil para la edición)
        context['avatar_form'] = avatar_form or FormularioPerfil(instance=user.perfil)
        
        return context

    def get(self, request, *args, **kwargs):
        # Muestra la página con los formularios inicializados
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        user = request.user
        
        # 1. Inicializar y manejar el formulario de datos de usuario
        user_form = CustomUserChangeForm(request.POST, instance=user)
        
        # 2. Inicializar y manejar el formulario de avatar (CRÍTICO: Incluir request.FILES)
        avatar_form = FormularioPerfil(request.POST, request.FILES, instance=user.perfil)

        # Verificar si ambos formularios son válidos
        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            # Guardamos el avatar
            avatar_form.save()
            
            # Agregamos un mensaje de éxito (usando el sistema de mensajes de Django)
            from django.contrib import messages
            messages.success(request, '¡Tu perfil y avatar han sido actualizados exitosamente!')
            
            return redirect(self.success_url)
        
        # Si no son válidos, renderiza la página con los errores en los formularios
        return render(request, self.template_name, self.get_context_data(user_form, avatar_form))
