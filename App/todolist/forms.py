from django import forms
from .models import Lista

class Formulario(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ["item", "completo"]