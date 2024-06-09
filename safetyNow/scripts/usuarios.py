from django.contrib.auth.models import User
import os
import django

# Configura la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'safetyNow.settings')

# Inicializa Django
django.setup()

# Función para crear usuarios
def crear_usuarios():
    # Lista de usuarios y contraseñas
    usuarios_contraseñas = [
        {'usuario': 'usuario1', 'contraseña': 'contraseña1'},
        {'usuario': 'usuario2', 'contraseña': 'contraseña2'},
        {'usuario': 'usuario3', 'contraseña': 'contraseña3'},
    ]
    
    # Iterar sobre la lista y crear los usuarios
    for datos_usuario in usuarios_contraseñas:
        usuario = datos_usuario['usuario']
        contraseña = datos_usuario['contraseña']
        User.objects.create_user(username=usuario, password=contraseña)

# Llamada a la función para crear usuarios
crear_usuarios()