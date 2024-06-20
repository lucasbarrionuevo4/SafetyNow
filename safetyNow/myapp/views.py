from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    print("Accediendo a la vista home...")
    return render(request, 'home.html')


def index(request):
    if request.method == 'POST':
        # Aquí obtienes el nombre de usuario y la contraseña del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autentica al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si las credenciales son válidas, haz login del usuario y redirige a la página de inicio
            login(request, user)
            return JsonResponse({'success': True}) 
        else:
            # Si las credenciales son inválidas, devuelve un mensaje de error
            return JsonResponse({'success': False, 'message': 'Usuario o contraseña incorrectos.'})
    else:
        # Renderiza el archivo HTML que contiene el formulario de inicio de sesión
        return render(request, 'index.html')
