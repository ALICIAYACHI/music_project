from django.db import models

class Album(models.Model):
    nombre = models.CharField(max_length=200)
    año = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.año})"


class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    duracion = models.CharField(max_length=20, blank=True)  # ej. "3:45"
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    album = models.ForeignKey(Album, related_name='canciones', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
