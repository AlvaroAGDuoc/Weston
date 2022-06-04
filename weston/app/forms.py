from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario



class RegistroUsuario(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'telefono', 'password1', 'password2']