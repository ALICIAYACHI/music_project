from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Cancion
from .forms import AlbumForm, CancionForm

# Albums
def lista_albumnes(request):
    albumnes = Album.objects.all().order_by('-año')
    return render(request, 'music/lista_albumnes.html', {'albumnes': albumnes})

def crear_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_albumnes')
    else:
        form = AlbumForm()
    return render(request, 'music/album_form.html', {'form': form})

def editar_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('lista_albumnes')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/album_form.html', {'form': form, 'album': album})

def eliminar_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('lista_albumnes')
    return render(request, 'music/album_confirm_delete.html', {'album': album})

# Canciones
def lista_canciones(request):
    canciones = Cancion.objects.select_related('album').all().order_by('-created_at')
    return render(request, 'music/lista_canciones.html', {'canciones': canciones})

def detalle_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    return render(request, 'music/detalle_cancion.html', {'cancion': cancion})

def crear_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_canciones')
    else:
        form = CancionForm()
    return render(request, 'music/cancion_form.html', {'form': form})

def editar_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    if request.method == 'POST':
        form = CancionForm(request.POST, request.FILES, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('detalle_cancion', cancion_id=cancion.id)
    else:
        form = CancionForm(instance=cancion)
    return render(request, 'music/cancion_form.html', {'form': form, 'cancion': cancion})

def eliminar_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id)
    if request.method == 'POST':
        cancion.delete()
        return redirect('lista_canciones')
    return render(request, 'music/cancion_confirm_delete.html', {'cancion': cancion})
