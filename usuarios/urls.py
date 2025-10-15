from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Vista de inicio de sesión de Django
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # Vista personalizada para el registro de usuarios.
    path('registro/', views.registro_usuario, name='registro'),
    
    # Vista de cierre de sesión de Django, redirigiendo al inicio
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    
    # URL UNIFICADA para gestionar el perfil/avatar (apunta a la vista 'perfil')
    path('perfil/', views.perfil, name='perfil'),
    
    # URL para cambiar la contraseña usando la vista genérica (apunta a CambiarContraseña CBV)
    path('cambiar_contrasena/', views.CambiarContraseña.as_view(), name='password_change'),
    
    # URL para el mensaje de éxito después de cambiar la contraseña.
    path('cambiar_contrasena/done/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='password_change_done'),
    
    path('editar/', views.EditarPerfil.as_view(), name='editar_perfil'),
]