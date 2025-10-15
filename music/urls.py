from django.urls import path
from . import views

urlpatterns = [
    # Albums
    path('albumnes/', views.lista_albumnes, name='lista_albumnes'),
    path('albumnes/nuevo/', views.crear_album, name='crear_album'),
    path('albumnes/<int:album_id>/editar/', views.editar_album, name='editar_album'),
    path('albumnes/<int:album_id>/eliminar/', views.eliminar_album, name='eliminar_album'),

    # Canciones
    path('canciones/', views.lista_canciones, name='lista_canciones'),
    path('canciones/nuevo/', views.crear_cancion, name='crear_cancion'),
    path('canciones/<int:cancion_id>/', views.detalle_cancion, name='detalle_cancion'),
    path('canciones/<int:cancion_id>/editar/', views.editar_cancion, name='editar_cancion'),
    path('canciones/<int:cancion_id>/eliminar/', views.eliminar_cancion, name='eliminar_cancion'),
]
