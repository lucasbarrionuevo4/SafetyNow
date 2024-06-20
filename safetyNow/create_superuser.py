import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'safetyNow.settings')

django.setup()

from django.contrib.auth.models import User

User.objects.create_superuser('admin2','email','contraseña')
print("Superusuario creado correctamente.")
