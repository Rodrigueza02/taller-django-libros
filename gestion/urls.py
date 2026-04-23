from django.urls import path
from . import views

urlpatterns = [
    # ---- HELEN: URLs de Autores ----
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.CrearAutorView.as_view(), name='crear_autor'),
    path('autores/editar/<int:pk>/', views.EditarAutorView.as_view(), name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.EliminarAutorView.as_view(), name='eliminar_autor'),
    ]