from django import forms
from .models import Periodista
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = ("titulo","resumen","palabras_clave","autor")

class PeriodistaForm(forms.ModelForm):
    
    class Meta:
        model = Periodista
        fields = ("nombre","apellido","dni","celular","direccion","correo")
