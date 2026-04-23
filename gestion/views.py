from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# =============================================
# HELEN: CRUD DE AUTORES
# =============================================

# Lista de autores — usamos función (sencilla)
def lista_autores(request):
    autores = Autor.objects.all().order_by('nombre')
    return render(request, 'gestion/lista_autores.html', {'autores': autores})

# Crear autor — usamos vista genérica (CreateView ya sabe cómo crear)
class CrearAutorView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('lista_autores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Autor'
        context['boton'] = 'Guardar Autor'
        return context

# Editar autor — usamos vista genérica (UpdateView ya sabe cómo editar)
class EditarAutorView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('lista_autores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Autor'
        context['boton'] = 'Actualizar Autor'
        return context

# Eliminar autor — usamos vista genérica (DeleteView ya sabe cómo eliminar)
class EliminarAutorView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_confirm_delete.html'
    success_url = reverse_lazy('lista_autores')