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
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True}) 
        else:
            return JsonResponse({'success': False, 'message': 'Usuario o contraseña incorrectos.'})
    else:
        return render(request, 'index.html')
    
def retirar(request):
    return render(request, 'retirar.html')

def consultar(request):
    return render(request, 'consultar.html')

def logout_view(request):
    return redirect('/')
