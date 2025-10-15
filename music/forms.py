from django import forms
from .models import Cancion, Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nombre', 'año']

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'duracion', 'portada', 'album']
