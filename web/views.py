from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from .forms import ContactoForm


#@login_required
def index(request):
    context = {
    }
    return render(request, 'index.html', context)

def contacto(request):
    return render(request, 'contact.html') 

#def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar los datos aquí (enviar email, guardar en DB, etc.)
            return render(request, 'contacto_exitoso.html')  # Redirigir a una página de éxito
    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})
