from django.urls import path
from . import views

urlpatterns = [
    # ---- HELEN: URLs de Autores ----
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.CrearAutorView.as_view(), name='crear_autor'),
    path('autores/editar/<int:pk>/', views.EditarAutorView.as_view(), name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.EliminarAutorView.as_view(), name='eliminar_autor'),

    # ---- TÚ: URLs de Libros ----
    path('libros/', views.ListaLibrosView.as_view(), name='lista_libros'),
    path('libros/crear/', views.CrearLibroView.as_view(), name='crear_libro'),
    path('libros/editar/<int:pk>/', views.EditarLibroView.as_view(), name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.EliminarLibroView.as_view(), name='eliminar_libro'),
]