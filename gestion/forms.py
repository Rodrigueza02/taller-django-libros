from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha de nacimiento'
    )

    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        labels = {
            'nombre': 'Nombre completo',
            'correo': 'Correo electrónico',
            'nacionalidad': 'Nacionalidad',
            'biografia': 'Biografía',
        }
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }