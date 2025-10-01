from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Vista de inicio de sesión de Django, con ruta de plantilla explícita
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # Vista personalizada para el registro de usuarios.
    path('registro/', views.registro_usuario, name='registro'),
    
    # Vista de cierre de sesión de Django.
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    
    # Vista personalizada para el perfil del usuario.
    path('perfil/', views.perfil_usuario, name='perfil'),
    
    # URL para la vista de edición de perfil.
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    
    # URL para cambiar la contraseña usando la vista genérica.
    path('cambiar_contrasena/', views.CambiarContraseña.as_view(), name='password_change'),
    
    # URL para el mensaje de éxito después de cambiar la contraseña.
    path('cambiar_contrasena/done/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='password_change_done'),
]