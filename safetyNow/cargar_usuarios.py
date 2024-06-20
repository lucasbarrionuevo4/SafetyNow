# load_data.py

import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'safetyNow.settings')
django.setup()

from myapp.models import Profile
from django.contrib.auth.models import User

# Crea usuarios y perfiles
user1 = User.objects.create_user(username='user1', password='pass1', email='user1@example.com')
profile1 = Profile.objects.create(user=user1, bio='Bio of user1')

user2 = User.objects.create_user(username='user2', password='pass2', email='user2@example.com')
profile2 = Profile.objects.create(user=user2, bio='Bio of user2')

print("Datos cargados exitosamente.")
