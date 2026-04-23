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
        
class LibroForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha de publicación'
    )

    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        labels = {
            'titulo': 'Título del libro',
            'genero': 'Género literario',
            'isbn': 'Código ISBN',
            'autor': 'Autor',
        }